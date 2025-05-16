from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import User

def create_test_user(username, password, first_name='', last_name='', email=''):
    return User.objects.create_user(
        username=username,
        password=password,
        first_name=first_name,
        last_name=last_name,
        email=email
    )

def authenticate_client(client, username, password):
    login_url = reverse('login')
    response = client.post(login_url, {
        'username': username,
        'password': password
    })
    assert response.status_code == status.HTTP_200_OK, "Login failed during test setup."

    sessionid = response.cookies.get('sessionid').value
    csrftoken = response.cookies.get('csrftoken').value if 'csrftoken' in response.cookies else ''

    client.cookies['sessionid'] = sessionid
    if csrftoken:
        client.cookies['csrftoken'] = csrftoken
        client.credentials(HTTP_X_CSRFTOKEN=csrftoken)


class SignupViewTestCase(APITestCase):
    def test_signup_success(self):
        url = reverse('signup')
        data = {
            "username": "JohnDoe",
            "password": "Jason_423",
            "first_name": "John",
            "last_name": "Doe",
            "email": "johndoe@email.com"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['username'], data['username'])
        self.assertEqual(response.data['email'], data['email'])
        self.assertEqual(response.data['first_name'], data['first_name'])
        self.assertEqual(response.data['last_name'], data['last_name'])

    def test_signup_missing_fields(self):
        url = reverse('signup')
        data = {
            'username': '',
            'email': '',
            'password': ''
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class LoginViewTestCase(APITestCase):
    def setUp(self):
        self.username = 'loginuser'
        self.password = 'securepassword'
        self.user = create_test_user(username=self.username, password=self.password)
        self.login_url = reverse('login')

    def test_login_success(self):
        data = {
            'username': self.username,
            'password': self.password
        }
        response = self.client.post(self.login_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], "Login realizado com sucesso.")

    def test_login_invalid_credentials(self):
        data = {
            'username': self.username,
            'password': 'wrongpassword'
        }
        response = self.client.post(self.login_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data['detail'], "Credenciais inválidas.")


class LogoutViewTestCase(APITestCase):
    def setUp(self):
        self.username = 'logoutuser'
        self.password = 'logoutpass123'
        self.user = create_test_user(username=self.username, password=self.password)
        self.logout_url = reverse('logout')

        authenticate_client(self.client, self.username, self.password)

    def test_logout_success(self):
        response_logout = self.client.post(self.logout_url)

        self.assertEqual(response_logout.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response_logout.data['message'], "Logout realizado com sucesso.")


class UserInfoViewTestCase(APITestCase):
    def setUp(self):
        self.username = 'user'
        self.password = 'pass123'
        self.first_name = 'John'
        self.last_name = 'Doe'
        self.email = "johndoe@email.com"
        self.user = create_test_user(
            username=self.username,
            password=self.password,
            first_name=self.first_name,
            last_name=self.last_name,
            email=self.email
        )
        self.user_info_url = reverse('user_info')

        authenticate_client(self.client, self.username, self.password)

    def test_user_info_fetch(self):
        response_info = self.client.get(self.user_info_url)

        self.assertEqual(response_info.status_code, status.HTTP_200_OK)
        self.assertEqual(response_info.data, {
            'id': self.user.id,
            'username': self.username,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'profile_picture': None
        })
