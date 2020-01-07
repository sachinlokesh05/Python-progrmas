name = "simple_oauth2"

import os
import logging
import time
from flask import Flask, request, redirect, session, render_template
import json
import jwt
from urllib.request import urlopen
from urllib.parse import quote_plus
from werkzeug.exceptions import Unauthorized, Forbidden


class OAuth():
    def __init__(self, app, settings, rbac):
        assert 'well_known_url' in settings, 'well_known_url not defined'
        assert 'client_id' in settings, 'client_id not defined'
        assert 'redirect_uri' in settings, 'redirect_uri not defined'
        assert 'audience' in settings, 'audience not defined'
        self.app = app
        with urlopen(settings['well_known_url']) as f:
            endpoints = f.read()
        self.settings = settings
        if 'whitelist' in settings:
            self.whitelist = settings['whitelist']
        else:
            self.whitelist = []
        self.endpoints = json.loads(endpoints.decode())
        self.token_url = self.endpoints['token_endpoint']
        self.keys_url = self.endpoints['jwks_uri']
        self.authorize_url = self.endpoints['authorization_endpoint']
        self.client_id = settings['client_id']
        self.redirecturi = quote_plus(settings['redirect_uri'])
        self.baseuri = settings['redirect_uri'].replace('/signin-oidc', '')
        if 'scopes' in settings:
            self.scopes = settings['scopes']
        else:
            self.scopes = ''
        self.audience = settings['audience']
        self.redirect_url = ''.join((self.authorize_url,
                                     '?client_id=', self.client_id,
                                     '&response_type=token',
                                     '&scope=', 'openid ', self.scopes,
                                     '&redirect_uri=', self.redirecturi,
                                     '&state=state',
                                     '&nonce=nonce'
                                     ))
        self.key_cache = {}
        self.rbac = rbac
        self.logger = logging.getLogger(__name__)

        app.before_request_funcs.setdefault(None, []).append(self.before)
        app.add_url_rule('/signin-oidc', 'signin-oidc', self.signin)

    def before(self):
        # avoid loops
        if request.url.startswith(self.settings['redirect_uri']):
            return
        # ignore whitelisted endpoints
        if request.full_path in self.whitelist:
            return
        # pass if already authenticated
        if self.is_authenticated():
            return
        # Check if we have a bearer token
        if self.check_bearer():
            return
        # redirect to identity server if client comes from a browser
        if self.is_browser():
            session['asked_url'] = request.url
            return self.redir()
        # I dunnow u
        raise Unauthorized('request not authenticated')

    def signin(self):
        self.logger.info(session['authenticated'])
        if 'token' in request.args:
            if self.parse_token(request.args['token']):
                if 'asked_url' in session:
                    return redirect(session['asked_url'])
                return redirect(self.baseuri)
        if 'error' in request.args:
            raise Unauthorized('request not authenticated')

        html = """<!DOCTYPE html>
            <html>
                <head>
                    <script>
                        try {
                            x = location.hash.split('&');
                            y = x[0].split('=');
                            if (y[1] != '#access_token') {
                                location.replace("$baseuri/sign-error?error=forbidden");
                            }
                            token = y[1]
                            location.replace("$baseuri/signin-oidc?token=" + token);
                        } catch(error) {
                            location.replace("$baseuri/sign-oidc?error=" + error);
                        }
                    </script>
                </head>
            </html>"""
        return html.replace('$baseuri', self.baseuri)


    def fetch_key(self, kid):
        """
        Check if the jwk key kid is cached so it returns it
        if not, query jwk key endpoint and put keys into cache
        """
        try:
            return self.key_cache[kid]
        except KeyError:
            pass

        with urlopen(self.keys_url) as f:
            data = f.read()
        data = json.loads(data.decode())
        for key in data['keys']:
            self.key_cache[key['kid']] = key

        try:
            return self.key_cache[kid]
        except KeyError:
            return None

    def parse_token(self, token):
        self.app.logger.info("parse_token")
        try:
            headers = jwt.get_unverified_header(token)
        except jwt.exceptions.DecodeError:
            return False

        pk = self.fetch_key(headers['kid'])
        if pk is None:
            return False

        pk = jwt.algorithms.RSAAlgorithm.from_jwk(json.dumps(pk))
        try:
            payload = jwt.decode(token, pk, audience=self.audience)
        except jwt.PyJWTError:
            self.app.logger.info('token not valid or expired')
            return False

        if payload['exp'] < time.time():
            return False

        for scope in self.scopes.split(' '):
            if scope not in payload['scp']:
                self.app.logger.info('required scope {} not found'.format(scope))
                return False

        session['authenticated'] = True
        session['client'] = payload['sub']
        session['token'] = token
        session['exp'] = payload['exp']
        return True

    def check_bearer(self):
        """
        Parse request headers and fetch Authorization key
        if present, check the existance of a bearer token
        decode the token and store the client_id an expiration in the session
        """

        session['authenticated'] = False

        if 'Authorization' not in request.headers:
            return False

        method, token = request.headers['Authorization'].split(' ')
        if method != 'Bearer':
            return False

        return self.parse_token(token)

    def is_authenticated(self):
        return 'authenticated' in session and session['authenticated'] and session['exp'] > time.time()

    def redir(self):
        return redirect(self.redirect_url, code=302)

    def authorize(self, operation):
        def decorated(func):
            def wrapper(*args, **kwargs):
                if not self.is_authenticated():
                    raise Unauthorized('request not authenticated')
                client = session['client']
                if not self.is_authorized(client, operation):
                    raise Forbidden(
                        'operation {} forbidden for client {}'.format(operation, client))
                return func(*args, **kwargs)
            return wrapper
        return decorated

    def is_browser(self):
        return 'USER_AGENT' in request.headers and request.headers['USER_AGENT'].startswith('Mozilla')

    def is_authorized(self, client, operation):
        if self.rbac is not None:
            return self.rbac(client, operation)
        return True

