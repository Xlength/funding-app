# funding/tests.py
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class SimpleTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')

    def test_login_and_access_apply_funding(self):
        login = self.client.login(username='testuser', password='password')

        self.assertTrue(login)

        response = self.client.get(reverse('apply_funding'))

        self.assertEqual(response.status_code, 200)
