from datetime import date
import pytest
from django.test import Client
from django.contrib.auth.models import User
from django.conf import settings
from museum.models  import ArtForm, Employee, Hall, Exhibition
import uuid


@pytest.fixture(autouse=True)
def django_db_setup():
    settings.DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
        'ATOMIC_REQUESTS': True,
    }

@pytest.fixture
def user():
    user = User.objects.filter(username='anon').first()
    return user

@pytest.fixture
def admin():
    user = User.objects.filter(username='vassyan').first()
    return user

@pytest.fixture
def client():
    client = Client()
    return client

@pytest.fixture
def exhibit_form_data():
    id = 'c69bf26e-4ac4-480a-bf78-1cb6cef35dee'
    name = 'test'
    art_form = [ArtForm.objects.all().first()]
    print(art_form)
    print('================================================================================')
    hall = Hall.objects.all().first()
    observer = Employee.objects.filter(hall= hall).first()
    exhibition = Exhibition.objects.filter(hall= hall).first()
    photo = 'https://iso.500px.com/wp-content/uploads/2016/03/stock-photo-142984111.jpg'

    return {
    'id' : id,
    'name' : name,
    'art_form' : art_form,
    'admission_date': date(2022,5,6),
    'observer': observer,
    'photo' : photo,
    'hall': hall,
    'exhibition': exhibition
}