from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed


class TestOcLettingSite:
    '''This classtest ...'''

    def test_index(self, client):
        response = client.get(reverse('index'))
        assert response.status_code == 200
        assertTemplateUsed(response, 'index.html')
