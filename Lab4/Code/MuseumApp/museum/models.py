from django.core.validators import MinLengthValidator
from django.db import models
from django.core.validators import RegexValidator

class Hall(models.Model):

    number = models.CharField(max_length=3, help_text="Enter hall number")

    name = models.CharField(max_length=20, help_text="Enter hall name")

    floor = models.CharField(max_length=3, help_text="Enter hall floor")

    area = models.PositiveIntegerField(help_text="Enter hall area")

    def __str__(self):
        return self.name




class Position(models.Model):
    name = models.CharField(max_length=20, help_text="Enter a position")

    def __str__(self):
        return self.name



from phonenumber_field.modelfields import PhoneNumberField

class Employee(models.Model):

    user_name = models.CharField(max_length=20, help_text="Enter user name")

    first_name = models.CharField(max_length=20, help_text="Enter full name")

    last_name = models.CharField(max_length=20, help_text="Enter last name")

    hall = models.ForeignKey('Hall', on_delete=models.CASCADE, related_name="employee")

    num_validetor = RegexValidator(regex=r"^\+375 \(29\) \d{3}-\d{2}-\d{2}$")

    phone_number = models.CharField(max_length=20, validators=[num_validetor], default='+375 (29) xxx-xx-xx')

    position = models.ForeignKey('Position', on_delete=models.CASCADE,related_name="employee")

    def __str__(self):
        return f"{self.last_name} {self.position}"



import uuid
from django.core.validators import MaxValueValidator, MinValueValidator 

class Excursion(models.Model):

    excursion_code = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular excursion")

    name = models.CharField(max_length=20, help_text="Enter excursion name")

    date = models.DateField()

    group_amount = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])

    guide = models.OneToOneField('Employee', on_delete=models.CASCADE)

    def __str__(self):
        return self.name



class ArtForm(models.Model):
    name = models.CharField(max_length=20, help_text="enter art form")

    def __str__(self):
        return self.name




class Exhibit(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular exhibit")

    name = models.CharField(max_length=20, help_text="enter Xzibit name")

    art_form = models.ManyToManyField('ArtForm')

    admission_date = models.DateField()

    observer = models.ForeignKey('Employee',on_delete=models.DO_NOTHING, related_name="exhibit")

    photo = models.URLField(default='')

    hall = models.ForeignKey('Hall', on_delete=models.CASCADE, related_name="exhibit")

    exposition = models.ForeignKey('Exposition', on_delete=models.DO_NOTHING, related_name="exhibit", null=True, blank=True)

    exhibition = models.ForeignKey('Exhibition', on_delete=models.DO_NOTHING, related_name="exhibit", null=True, blank=True)

    def display_art_form(self):
        return ', '.join([ art_form.name for art_form in self.art_form.all()[:3] ])
    display_art_form.short_description = 'Art form'

    def __str__(self):
        return self.name

class Exposition(models.Model):
    name = models.CharField(max_length=20, help_text="enter exposition name")

    theme = models.ForeignKey('Theme', on_delete=models.CASCADE, related_name="exposition")

    hall = models.ManyToManyField('Hall')

    def __str__(self):
        return self.name
    



class Exhibition(models.Model):
    name = models.CharField(max_length=20, help_text="enter exhibition name")

    theme = models.ForeignKey('Theme', on_delete=models.CASCADE, related_name="exhibition")

    hall = models.ManyToManyField('Hall')

    date = models.DateField()

    def __str__(self):
        return self.name
    


class Theme(models.Model):
    name = models.CharField(max_length=20, help_text="enter exposition name")

    def __str__(self):
        return self.name



