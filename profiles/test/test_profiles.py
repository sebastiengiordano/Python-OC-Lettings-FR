from django.urls import reverse
import pytest


@pytest.mark.django_db
@pytest.mark.parametrize(
    'url, apps',
    [['profiles:index', ('home:index', 'lettings:index')]])
def test_profiles_index(client, url, apps, create_test_profiles):
    url = reverse(url)
    urls_redirection_apps = [reverse(app) for app in apps]

    response = client.get(url)

    assert response.status_code == 200

    assert b"<title>Profiles</title>" in response.content
    assert b"<h1>Profiles</h1>" in response.content

    for profile in create_test_profiles:
        assert f"""<a href="{url}{profile.user.username}/">""".encode('utf-8') in response.content

    for url in urls_redirection_apps:
        assert f"""<a href="{url}">""".encode('utf-8') in response.content


@pytest.mark.django_db
@pytest.mark.parametrize(
    'profiles_url, apps',
    [
        ['profiles:profile',
         ('profiles:index', 'home:index', 'lettings:index')
        ]
    ])
def test_profiles_detail(client, profiles_url, apps, create_test_profiles):
    urls_redirection_apps = [reverse(app) for app in apps]

    for profile in create_test_profiles:
        url = reverse(
            profiles_url,
            kwargs={'username': profile.user.username})
        response = client.get(url)

        assert response.status_code == 200

        assert f"""<title>{profile.user.username}</title>""".encode('utf-8') in response.content
        assert f"""<h1>{profile.user.username}</h1>""".encode('utf-8') in response.content

        user = profile.user
        user_detail = [
            f"First name: {user.first_name}",
            f"Last name: {user.last_name}",
            f"Email: {user.email}",
            f"Favorite city: {profile.favorite_city}"]
        for information in user_detail:
            assert f"""<p>{information}</p>""".encode('utf-8') in response.content

        for url_app in urls_redirection_apps:
            assert f"""<a href="{url_app}">""".encode('utf-8') in response.content
