# forms.py
from datetime import date
from django import forms

from museum.models import Employee, Exhibit, Exhibition, Hall
class EmployeeForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Employee
        fields = '__all__'

class ExhibitForm(forms.ModelForm):

    def clean(self):
            admission_date = self.cleaned_data.get('admission_date')
            hall = self.cleaned_data.get('hall')
            observer = self.cleaned_data.get('observer')
            exhibition = self.cleaned_data.get('exhibition')

            if admission_date > date.today():
                raise forms.ValidationError("Admission date are incorrect")
            
            if hall != observer.hall:
                raise forms.ValidationError("Exhibit hall and observer hall are different")
            
            if exhibition and exhibition.date < admission_date:
                raise forms.ValidationError("Admission date are greater then exhibition date")
 
            
            return self.cleaned_data
    
    class Meta:
         model = Exhibit
         fields = '__all__'
