from django.urls import reverse
import pytest


@pytest.mark.django_db
@pytest.mark.parametrize(
    'url, apps',
    [['lettings:index', ('home:index', 'profiles:index')]])
def test_lettings_index(client, url, apps, create_test_address, create_test_letting):
    url = reverse(url)
    urls_redirection_apps = [reverse(app) for app in apps]

    response = client.get(url)

    assert response.status_code == 200

    assert b"<title>Lettings</title>" in response.content
    assert b"<h1>Lettings</h1>" in response.content

    for letting in create_test_letting:
        assert f"""<a href="{url}{letting.id}/">""".encode('utf-8') in response.content

    for url in urls_redirection_apps:
        assert f"""<a href="{url}">""".encode('utf-8') in response.content


@pytest.mark.django_db
@pytest.mark.parametrize(
    'lettings_url, apps',
    [
        ['lettings:letting',
         ('lettings:index', 'home:index', 'profiles:index')
        ]
    ])
def test_lettings_detail(client, lettings_url, apps,
                          create_test_address,
                          create_test_letting):
    urls_redirection_apps = [reverse(app) for app in apps]

    for letting in create_test_letting:
        url = reverse(
            lettings_url,
            kwargs={'letting_id': letting.id})
        response = client.get(url)

        assert response.status_code == 200

        assert f"""<title>{letting.title}</title>""".encode('utf-8') in response.content
        assert f"""<h1>{letting.title}</h1>""".encode('utf-8') in response.content

        address = letting.address
        address_detail = [
            str(address),
            f"{address.city}, {address.state} " f"{address.zip_code}",
            f"{address.country_iso_code}"]
        for information in address_detail:
            assert f"""<p>{information}</p>""".encode('utf-8') in response.content

        for url_app in urls_redirection_apps:
            assert f"""<a href="{url_app}">""".encode('utf-8') in response.content
