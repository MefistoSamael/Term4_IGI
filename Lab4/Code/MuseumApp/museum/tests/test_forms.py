from datetime import date
import pytest
from museum.forms import ExhibitForm


@pytest.mark.django_db
def test_exhibit_form(exhibit_form_data, admin, client):
    client.force_login(admin)
    
    form = ExhibitForm(data=exhibit_form_data)
    assert form.is_valid()

    data = exhibit_form_data
    data['admission_date']=date.today()

    form = ExhibitForm(data=data)
    assert not form.is_valid()


