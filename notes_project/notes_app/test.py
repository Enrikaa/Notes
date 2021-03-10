from django.test import TestCase
from django.contrib.auth.models import User
from django.test import Client

from .models import Account


class AuthTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user("User", "user@gmail.com", "856921")
        self.client = Client()

    def test_login_works_as_expected(self):
        """ Testing th authentication of the user """
        response = self.client.post(
            "/user_login", data={"username": "163", "password": "852"}
        )
        print(response.status_code)
        assert response.status_code == 200

    def test_inactive_user_cannot_login(self):
        """ Testing if user can't login if it is inactive """
        pass