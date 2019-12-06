"""
this file is created for test cases, test case for registrations and login apis are ran 
"""

import json
import requests
from django.contrib.auth.models import User
from django.test import TestCase, override_settings
from django.urls import reverse
from fundoo.settings import BASE_URL
from user.models import Registration


class ModelTest(TestCase):
    fixtures = ['test_fundoo_db']

    def test_label_string_representation1(self):
        entry = Registration(name="My name")
        self.assertEqual(str(entry), entry.name)

    def test_label_string_representation2(self):
        entry = Registration(name="My name")
        self.assertNotEqual(str(entry), "")

    def test_label_equal1(self):
        user1 = Registration(name="sachin")
        user2 = Registration(name="sachin")
        self.assertTrue(user1 == user2, True)

    def test_label_equal2(self):
        user1 = Registration(name="sachin")
        user2 = Registration(name="deepak ")
        self.assertFalse(user1 == user2, True)

    def test_label_isinstance1(self):
        user1 = User(username="sachin")
        user2 = Registration(name="sachin ")
        self.assertEqual(user1 == user2, False)

    def test_label_isinstance2(self):
        user1 = User(username="deepak")
        user2 = Registration(name="deepak ")
        self.assertFalse(user1 == user2, "hi")

    def test_label_verbose_name_plural1(self):
        self.assertEqual(
            str(Registration._meta.verbose_name_plural), "user details")

    def test_label_verbose_name_plural2(self):
        self.assertNotEqual(
            str(Registration._meta.verbose_name_plural), "testing")

    def test_label_verbose_name1(self):
        self.assertEqual(str(Registration._meta.verbose_name), "user detail")

    def test_label_verbose_name2(self):
        self.assertNotEqual(str(Registration._meta.verbose_name), "testing")




    def test_registration1(self):
        url = BASE_URL + reverse('registration')
        resp = self.client.post(
            url, {'username': '', 'password': 'admin', 'email': 'sachin.beee.15@acharya.ac.in'})
        # print(resp.META)
        self.assertEqual(resp.status_code, 400)

    def test_registration2(self):
        url = BASE_URL + reverse('registration')
        resp = self.client.post(
            url, {'username': 'admin', 'password': 'admin', 'email': 'sachin.beee.   15@acharya.ac.in'})
        # print(resp.META)
        self.assertEqual(resp.status_code, 400)

    def test_registration3(self):
        url = BASE_URL + reverse('registration')
        resp = self.client.post(
            url, {'username': 'hello', 'password': 'world', 'email': 'now@gmail.com'})
        # print(resp.META)
        self.assertEqual(resp.status_code, 201)

    def test_login1(self):
        url = BASE_URL + reverse('login')
        resp = self.client.post(
            url, {'username': 'admin', 'password': 'admin'}, )
        self.assertEqual(resp.status_code, 201)

    def test_login2(self):
        url = BASE_URL + reverse('login')
        resp = self.client.post(url, {'username': 'rfg', 'password': 'fg'}, )
        self.assertEqual(resp.status_code, 400)

    def test_forgotpassword2(self):
        url = BASE_URL + reverse('forgotPassword')
        resp = self.client.post(url, {'email': 'sachinsanju04@gmail.com'}, )
        self.assertEqual(resp.status_code, 201)

    def test_forgotpassword3(self):
        url = BASE_URL + reverse('forgotPassword')
        resp = self.client.post(url, {'email': 'sachin'}, )
        self.assertEqual(resp.status_code, 400)

    def test_logout1(self):
        url = BASE_URL + reverse('logout')
        resp = self.client.get(url, )
        self.assertEqual(resp.status_code, 200)





