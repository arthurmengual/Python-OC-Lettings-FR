import pytest
from django.urls import reverse
from lettings.models import Letting, Address
from pytest_django.asserts import assertTemplateUsed


@pytest.fixture
def lettings_fixture():
    address = Address.objects.create(
        number="0",
        street="street",
        city="city",
        state="state",
        zip_code="98",
        country_iso_code="7",
    )
    letting = Letting.objects.create(title="title", address=address)
    return letting


@pytest.mark.django_db
class TestLettings:
    """This is the testclass for index_view"""

    def test_index(self, client, lettings_fixture):
        """This test ....."""
        response = client.get(reverse("lettings:index"))
        assert response.context["lettings_list"][0] == lettings_fixture
        assert response.status_code == 200
        assertTemplateUsed(response, "lettings/index.html")
        assert b'<title>Lettings</title>' in response.content

    def test_letting(self, client, lettings_fixture):
        """This test ..."""
        response = client.get(
            reverse("lettings:letting", kwargs={"letting_id": lettings_fixture.id})
        )
        assert response.context["title"] == lettings_fixture.title
        assert response.context["address"] == lettings_fixture.address
        assert response.status_code == 200
        assertTemplateUsed(response, "lettings/letting.html")
        assert b'<title>title</title>' in response.content
        # comment faire un genre de f string avec b'
