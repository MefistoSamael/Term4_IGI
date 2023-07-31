# forms.py
from datetime import date
import logging
from django import forms

from museum.models import Employee, Exhibit, Exhibition, Hall

logger = logging.getLogger(__name__)

class ExhibitForm(forms.ModelForm):

    def clean(self):
            admission_date = self.cleaned_data.get('admission_date')
            hall = self.cleaned_data.get('hall')
            observer = self.cleaned_data.get('observer')
            exhibition = self.cleaned_data.get('exhibition')

            if admission_date > date.today():
                logger.error(f'Failed to create exhibit - admission date are incorrect')
                raise forms.ValidationError("Admission date are incorrect")
            
            if hall != observer.hall:
                logger.error(f'Failed to create exhibit - exhibit hall and observer hall are different')
                raise forms.ValidationError("Exhibit hall and observer hall are different")
            
            if exhibition and exhibition.date < admission_date:
                logger.error(f'Failed to create exhibit - admission date are greater then exhibition date')
                raise forms.ValidationError("Admission date are greater then exhibition date")
            
            logger.info(f'user input passed custom validation')
            
            return self.cleaned_data
    
    class Meta:
         model = Exhibit
         fields = '__all__'
