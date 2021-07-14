from apps.accounts.models import CustomUser


def test_custom_user_class(custom_user):
    assert isinstance(custom_user, CustomUser)


def test_custom_user_create(custom_user):
    assert CustomUser.objects.count() == 1
