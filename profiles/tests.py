import pytest
from django.urls import reverse
from .models import Profile
from pytest_django.asserts import assertTemplateUsed
from django.contrib.auth.models import User


@pytest.fixture
def profiles_fixture():
    user = User.objects.create(username='TestClient')
    profile = Profile.objects.create(user=user, favorite_city='city')
    return profile


@pytest.mark.django_db
class TestLettings:
    '''This is the testclass...'''

    def test_index(self, client, profiles_fixture):
        '''This test ...'''
        response = client.get(reverse('profiles:index'))
        assert response.context['profiles_list'][0] == profiles_fixture
        assert response.status_code == 200
        assertTemplateUsed(response, 'profiles/index.html')

    def test_profile(self, client, profiles_fixture):
        '''This test ...'''
        response = client.get(reverse('profiles:profile', kwargs={
                              'username': profiles_fixture.user.username}))
        assert response.context['profile'] == profiles_fixture
        assert response.status_code == 200
        assertTemplateUsed(response, 'profiles/profile.html')
