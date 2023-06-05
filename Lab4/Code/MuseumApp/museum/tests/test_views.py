import pytest
from django.urls import reverse
from constants import NONUSER_VIEWS, USER_VIEWS


@pytest.mark.parametrize('view', NONUSER_VIEWS)
@pytest.mark.django_db
def test_nonuser_access(user, admin, client, view):
    if isinstance(view, tuple):
        response = client.get(reverse(view[0], kwargs={'id': view[1]}))
    else:
        response = client.get(reverse(view))
    assert response.status_code == 200

    client.force_login(user)
    if isinstance(view, tuple):
        response = client.get(reverse(view[0], kwargs={'id': view[1]}))
    else:
        response = client.get(reverse(view))
    assert response.status_code == 200

    client.force_login(admin)
    if isinstance(view, tuple):
        response = client.get(reverse(view[0], kwargs={'id': view[1]}))
    else:
        response = client.get(reverse(view))
    assert response.status_code == 200


@pytest.mark.parametrize('view', USER_VIEWS)
@pytest.mark.django_db
def test_user_access(user, client, view):
    if isinstance(view, tuple):
        response = client.get(reverse(view[0], kwargs={'id': view[1]}))
    else:
        response = client.get(reverse(view))
    assert response.status_code == 302

    client.force_login(user)
    if isinstance(view, tuple):
        response = client.get(reverse(view[0], kwargs={'id': view[1]}))
    else:
        response = client.get(reverse(view))
    assert response.status_code == 200
