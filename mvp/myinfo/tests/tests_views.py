import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

# Initialize the APIClient for testing
client = APIClient()


@pytest.mark.django_db
def test_myinfo_get_authorise_url():
    session_cookie = 'testsessionid123'
    client.cookies['sessionid'] = session_cookie

    url = reverse('authorise_url')
    response = client.get(url)
    assert 'https://' in response.data['data']
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_myinfo_post_get_auth_code():
    session_cookie = 'testsessionid123'
    client.cookies['sessionid'] = session_cookie
    data = {"auth_code": "test_auth_code"}

    url = reverse('person_data')
    response = client.post(url, data, format='json')

    assert response.status_code == status.HTTP_200_OK
