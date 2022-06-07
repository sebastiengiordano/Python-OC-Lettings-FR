import pytest
from lettings.models import Letting, Address


@pytest.fixture
def address__data_for_test():
    return [
        {
            'number': '1',
            'street': 'Calle Cesar González',
            'city': 'Adjuntas',
            'state': 'Puerto Rico',
            'zip_code': '00601',
            'country_iso_code': '630'
        },
        {
            'number': '2',
            'street': 'Agawam',
            'city': 'Massachusetts',
            'state': 'USA',
            'zip_code': '01001',
            'country_iso_code': '840'
        },
        {
            'number': '8',
            'street': 'Pasteur',
            'city': 'Aulnay-sous-bois',
            'state': 'France',
            'zip_code': '96300',
            'country_iso_code': '250'
        }
    ]


@pytest.fixture
def letting__data_for_test():
    return [
        'title_one',
        'title_two',
        'title_three']


@pytest.fixture
def create_test_address(address__data_for_test):
    for address in address__data_for_test:
        Address.objects.create(**address)
    return Address.objects.all()


@pytest.fixture
def create_test_letting(letting__data_for_test):
    for address, title in zip(Address.objects.all(), letting__data_for_test):
        Letting.objects.create(title=title, address=address)
    return Letting.objects.all()
