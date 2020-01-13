from django.test import TestCase

# Create your tests here.import json
import pdb

import pytest
import requests
from django.contrib.auth.models import User

from fundoo.settings import BASE_URL, TEST_TOKEN
from django.test import Client, override_settings
from lib.token import token_validation

from django.test import TestCase
from django.urls import reverse


from blog.models import Post
import unittest


class NotesTest(TestCase):
    fixtures = ['test_fundoo_db']

    def test_note_getall1(self):
        url = BASE_URL + reverse('notes')
        resp = self.client.get(url, content_type='application/json', **header)
        self.assertEqual(resp.status_code, 200)

    def test_note_get1(self):
        url = BASE_URL + reverse('note_update', args=["fghjk])
        resp = self.client.get(url, content_type='application/json', **header)
        # print(resp.META)
        self.assertEqual(resp.status_code, 404)

    def test_note_post23(self):
        url = BASE_URL + reverse('notes')
        data = {"title": "hii", "note": "heelo", "is_archive": 'true'}
        resp = self.client.post(
            url, data, content_type='application/json', **header)
        self.assertEqual(resp.status_code, 201)

    def test_note_post3(self):
        url = BASE_URL + reverse('notes')
        data = {"title": "hii", "note": "heelo",
                "collaborators": ["nk90600@gmail.com"]}
        resp = self.client.post(
            url, data, content_type='application/json', **header)
        self.assertEqual(resp.status_code, 201)

    def test_note_post4(self):
        url = BASE_URL + reverse('notes')
        data = {"title": "hii", "note": "heelo", "url": "google.com"}
        resp = self.client.post(
            url, data, content_type='application/json', **header)
        self.assertEqual(resp.status_code, 400)

    def test_note_put2(self):
        url = BASE_URL + reverse('note_update', args=[1])
        data = {"title": "hii", "note": "heelo", }
        resp = self.client.put(
            url, data, content_type='application/json', **header)
        self.assertEqual(resp.status_code, 200)

    def test_note_delete1(self):
        url = BASE_URL + reverse('note_update', args=[500])
        resp = self.client.delete(
            url, content_type='application/json', **header)
        # print(resp.META)
        self.assertEqual(resp.status_code, 404)

    def test_note_delete2(self):
        url = BASE_URL + reverse('note_update', args=[1])
        resp = self.client.delete(
            url, content_type='application/json', **header)
        # print(resp.META)
        self.assertEqual(resp.status_code, 201)

    def test_search1(self):
        url = BASE_URL + reverse('search')
        data = {"ti": "japan", }
        resp = self.client.post(
            url, data, content_type='application/json', **header)
        self.assertEqual(resp.status_code, 400)

    def test_search2(self):
        url = BASE_URL + reverse('search')
        data = {"note": "japan", }
        resp = self.client.post(
            url, data, content_type='application/json', **header)
        self.assertEqual(resp.status_code, 200)
