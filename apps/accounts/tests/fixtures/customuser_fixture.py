import pytest

from apps.accounts.models import CustomUser


@pytest.fixture
def custom_user(db):
    return CustomUser.objects.create_user(
        username="johndoe",
        password="secret",
        email="jondoe@lojacorr.com",
        first_name="Jon",
        last_name="Doe",
    )
