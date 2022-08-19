import pytest
from django.contrib.auth.models import User
from profiles.models import Profile


@pytest.fixture
def profile__data_for_test():
    return [
        {
            'user': {
                'username': 'First_user',
                'first_name': 'Cesar',
                'last_name': 'González',
                'email': 'cesar.gonzalez@email_address.com'
            },
            'favorite_city': 'Adjuntas'
        },
        {
            'user': {
                'username': 'Second_user',
                'first_name': 'Guido',
                'last_name': 'Van Rossum',
                'email': 'guido.van.rossum@email_address.com'
            },
            'favorite_city': 'Massachusetts'
        },
        {
            'user': {
                'username': 'admin',
                'first_name': 'First Name',
                'last_name': 'Last Name',
                'email': 'admin@email_address.com'
            },
            'favorite_city': 'Lima'
        }
    ]


@pytest.fixture
def create_test_profiles(profile__data_for_test):
    for user_data in profile__data_for_test:
        user = User.objects.create(**user_data['user'])
        Profile.objects.create(
            user=user,
            favorite_city=user_data['favorite_city'])
    return Profile.objects.all()
