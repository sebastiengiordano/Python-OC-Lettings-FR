from django.urls import reverse
import pytest


@pytest.mark.parametrize(
    'home_url, apps',
    [
        ['home:index',
         ('profiles:index', 'lettings:index')]
    ])
def test_home_index(client, home_url, apps):
    home_url = reverse(home_url)
    urls_redirection_apps = [reverse(app) for app in apps]

    response = client.get(home_url)

    assert response.status_code == 200

    assert b"<title>Holiday Homes</title>" in response.content
    assert b"<h1>Welcome to Holiday Homes</h1>" in response.content

    for url in urls_redirection_apps:
        assert f"""<a href="{url}">""".encode('utf-8') in response.content
