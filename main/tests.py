from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import *
from accounts.models import *

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


class ExerciseViewTests(APITestCase):
    def setUp(self):
        self.username = 'logoutuser'
        self.password = 'logoutpass123'
        self.user = create_test_user(
            username=self.username,
            password=self.password,
            first_name='',
            last_name='',
            email=''
        )
        self.exercise_url = reverse('exercises-list')
        authenticate_client(self.client, self.username, self.password)

    def test_list_exercises(self):
        Exercise.objects.create(name='Push Up')
        Exercise.objects.create(name='Pull Up')

        response = self.client.get(self.exercise_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        self.assertEqual(len(response.data), 2)
