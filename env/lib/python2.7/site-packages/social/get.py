#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
get.py
======

A collection of functions to query social networks.

This is all very basic, but split out from another project, hence making it
easier to maintain.

Most of the functions are based on somebody elses findings, in particular:
https://gist.github.com/jonathanmoore/2640302
Was very helpful to implement most of the functions.
"""

import logging
import requests
import json

logger = logging.getLogger(__name__)


def facebook(url):
    """
    .. py:function:: facebook(url)

        Get the number of shares, likes and comments on facebook
        for the provided URL.

        :param str url: The url to query Facebook for.
        :return: the number of shares, likes and comments
        :rtype: Tuple
        :raises Exception: If the Facebook API responds with
                    anything other than `HTTP 200`.
    """
    facebook_count = \
        'http://graph.facebook.com/?ids=%s'
    query = facebook_count % (url)
    resp = requests.get(query)

    if resp.status_code in (200, 304):
        js = json.loads(resp.text)
        return (
            js.get('shares', 0),
            js.get('likes', 0),
            js.get('comments', 0),
        )
    elif resp.status_code in (404,):
        return (0, 0, 0,)
    else:
        raise Exception("Status: %s" % resp.status_code)


def linkedin(url):
    """
    .. py:function:: linkedin(url)

        Get the number of shares on linkedin for the provided URL.

        :param str url: The url to query Linkedin for.
        :return: the number of shares
        :rtype: Tuple
        :raises Exception: If the Linkedin API responds with
                    anything other than `HTTP 200`.
    """
    linkedin_count = \
        "https://www.linkedin.com/countserv/count/share?url=%s&format=json"
    query = linkedin_count % (url)
    resp = requests.get(query)

    if resp.status_code in (200, 304):
        return (
            json.loads(resp.text)['count'],
        )
    else:
        raise Exception("Status: %s" % resp.status_code)


def plusone(url):
    """
    .. py:function:: plusone(url)

        Get the number of plusones for the provided URL from Google+.

        :param str url: The url to query Goolge+ for.
        :return: the number of plusones.
        :rtype: Tuple
        :raises Exception: If the Google API responds with
                    anything other than `HTTP 200`.


    .. ToDo:: broken.
    """
    queryurl = "https://clients6.google.com/rpc"
    params = {
        "method": "pos.plusones.get",
        "id": "p",
        "params": {
            "nolog": True,
            "id": "%s" % (url),
            "source": "widget",
            "userId": "@viewer",
            "groupId": "@self",
        },
        "jsonrpc": "2.0",
        "key": "p",
        "apiVersion": "v1"
    }
    headers = {
        'Content-type': 'application/json',
    }
    result = 0
    try:
        resp, content = requests.post(
            queryurl,
            data=json.dumps(params),
            headers=headers
            )
        if resp.status_code in (200, 304):
            result_json = json.loads(resp.text)
            result = int(
                result_json['result']['metadata']['globalCounts']['count']
            )
            logger.debug("stop: counting +1s. Got %s.", result)
    except ValueError as e:
        logger.error(e)
        logger.error(json.dumps(params))
        logger.error(headers)
    except Exception as e:
        logger.error("""stop: counting +1s. Something weird happened.\n
                     %s
                     """ % e)
    except KeyError as e:
        raise KeyError(e)

    return (result, )


def stumbleupon(url):
    """
    .. py:function:: stumbleupon(url : string)

    :return: the number of tweets
    :rtype: Tuple
    :rtype: Tuple
    :raises Exception: If the stumbleupon API responds with
                    anything other than `HTTP 200`.
    """
    stumbleupon = \
        "http://www.stumbleupon.com/services/1.01/badge.getinfo?url=%s"
    query = stumbleupon % (url)
    resp = requests.get(query)

    if resp.status_code == 200:
        js = json.loads(resp.text)
        if 'result' in js:
            if 'views' in js['result']:
                return js['result']['views']
            else:
                return (0, )
    else:
        raise Exception


def tweets(url):
    """
    .. py:function:: tweets(url : string)

        Get the number of tweets containing the provided URL.

        This was deprecated as of November 20. 2015. See here:
        https://blog.twitter.com/2015/hard-decisions-for-a-sustainable-platform

        Hence, this function always returns (0,) until implemented otherwise.

        :param str url: The url to query Twitter for.
        :return: the number of tweets
        :rtype: Tuple
        :raises Exception: none.
        .. todo: Implement an own counter for URLs through the recommended
        "filter" Streaming-API.

        Old query:
        query = "http://urls.api.twitter.com/1/urls/count.json?url=%s" % (url)
    """
    return (0, )
