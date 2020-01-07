#!/usr/bin/env python
# -*- coding: utf-8

"""
:mod:`question.facebook` -- Tell facebook about user questions.


Requires Facebook Permission: `publish_actions`

Action (Answer a question)
##########################

Create
======

https://graph.facebook.com/me/pramari:answer?
access_token=ACCESS_TOKEN&
method=POST&
question=http%3A%2F%2Fsamples.ogp.me%2F362944703888607

Read
====

https://graph.facebook.com/me/pramari:answer?
access_token=ACCESS_TOKEN&
method=GET

Update
======

https://graph.facebook.com/{id_from_create_call}?
access_token=ACCESS_TOKEN&
method=POST&
question=http%3A%2F%2Fsamples.ogp.me%2F362944703888607

Delete
======

https://graph.facebook.com/{id_from_create_call}?
access_token=ACCESS_TOKEN&
method=DELETE

Object (Question)
#################

Create
======

https://graph.facebook.com/me/objects/pramari:question?
access_token=ACCESS_TOKEN&
method=POST&
object=%7B%22og%3Aurl%22%3A%22http%3A%5C%2F%5C%2Fsamples.ogp.me%5C%2F362944703888607%22%2C%22og%3Atitle%22%3A%22Sample+Question%22%2C%22og%3Atype%22%3A%22pramari%3Aquestion%22%2C%22og%3Aimage%22%3A%22https%3A%5C%2F%5C%2Ffbstatic-a.akamaihd.net%5C%2Fimages%5C%2Fdevsite%5C%2Fattachment_blank.png%22%2C%22og%3Adescription%22%3A%22%22%2C%22fb%3Aapp_id%22%3A362904360559308%7D


.. moduleauthor:: Andreas Neumeier <andreas@neumeier.org>
"""

from django.conf import settings
from requests_oauthlib import OAuth2Session
from requests_oauthlib.compliance_fixes import facebook_compliance_fix
import json

try:
    from exceptions import NotImplementedError
except:
    # we're on pyton3
    pass

if settings.DEBUG:
    redirect_uri = 'https://localhost/'
else:
    redirect_uri = 'http://www.pramari.de/'


class Facebook(object):
    def __init__(self, user):
        self.fb = OAuth2Session(
            settings.SOCIAL_AUTH_FACEBOOK_KEY,
            redirect_uri=redirect_uri
        )
        self.fb = facebook_compliance_fix(self.fb)
        self.accounts = user.social_auth.filter(provider="facebook")

    def create_question(self, question):
        """
        object is json for:
            urllib.unquote(url).decode('utf8')
            {
            "og:url":"http:\/\/samplesogp.me\/362944703888607",
            "og:title":"Sample+Question",
            "og:type":"pramari:question",
            "og:image":"https:\/\/fbstatic-a.akamaihd.net\/images\/devsite\/attachment_blank.png",
            "og:description":"",
            "fb:app_id":362904360559308
            }

        Usage:
        >>> from django.contrib.auth.models import User
        >>> from question.facebook import Facebook
        >>> from question.models import Question
        >>> u = User.objects.get(pk=1)
        >>> f = Facebook(u)
        >>> q = Question.objects.get(pk=1)
        >>> f.create_question(q)

        """

        url = """https://graph.facebook.com/me/objects/pramari:question"""
        data = {
            "og:url": question.get_absolute_url(),
            "og:title": question.question,
            "og:type": "pramari:question",
            "og:image": "https:\/\/fbstatic-a.akamaihd.net\/images\/devsite\/attachment_blank.png",
            "og:description": "",
            "fb:app_id": 362904360559308,
        }

        result = []
        for account in self.accounts:
            payload = {
                "access_token": account.extra_data['access_token'],
                "method": "POST",
                "object": json.dumps(data),
            }

            result += self.fb.post(
                url,
                params=payload
            )
        return result

    def create_answer(self, answer):
        raise NotImplementedError

    def update_timeline(self, message):

        for account in self.accounts:
            url = "https://graph.facebook.com/%s/feed" % (account.uid)
            payload = {'message': "%s" % (message)}

            result = self.fb.post(
                url,
                params={'access_token': account.extra_data['access_token']},
                data=json.dumps(payload)
            )

            return result.json()
