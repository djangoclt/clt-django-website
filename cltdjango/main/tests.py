from django.test import TestCase
from django.core.urlresolvers import resolve

from . import views


class MainUrlTest(TestCase):

    def test_home_url(self):
        url = resolve('/')

        self.assertEqual(url.func, views.index)
        self.assertEqual(url.url_name, 'index')

        resp = self.client.post('/')
        self.assertEqual(resp.status_code, 200)

    def test_active_members_url(self):
        url = resolve('/active-members/')

        self.assertEqual(url.func, views.active_members)
        self.assertEqual(url.url_name, 'active_members')

        resp = self.client.post('/active-members/')
        self.assertEqual(resp.status_code, 200)

    def test_page_not_found(self):
        resp = self.client.post('/does-not-exist/')
        self.assertEqual(resp.status_code, 404)
