"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
import json
import datetime

from django.conf import settings
settings.DEBUG = True

from django.test import TestCase

class BaseApiTest(TestCase):
    def get_json(self, url, status_code):
        response = self.client.get(url)
        self.assertEqual(response.status_code, status_code,
                         response.content)
        response_json = json.loads(response.content)
        return response_json


class MyAppTest(TestCase):

    def test_simple_post(self):

        my_data = {'somefield': 'Foo'}

        response = self.client.post('/api/v1/mymodel/',
                                    json.dumps(my_data),
                                    content_type='application/json')

        self.assertEquals(response.status_code, 201, response.content)
    
    def test_full_post(self):

        my_data = {'somefield': 'Foo',
                   'myextramodel': {'extra_field': 'Bar'}}

        response = self.client.post('/api/v1/mymodel/',
                                    json.dumps(my_data),
                                    content_type='application/json')

        self.assertEquals(response.status_code, 201, response.content)
