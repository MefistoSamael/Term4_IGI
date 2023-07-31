from datetime import datetime, timedelta, date
from django.contrib import admin
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.http import Http404

from museum.forms import ExhibitForm
from .models import ArtForm, Employee, Excursion, Exhibit, Exhibition, Exposition, Hall, Position, Theme
import re

@receiver(post_save, sender=Employee)
def create_user(sender, instance, created, **kwargs):
    if created:
        # Создание пользователя с такими же данными как у работника
        try:
            User.objects.create_user(instance.user_name, "", "111111111")
        except:
            raise Http404('User with such username alredy exsited')

        
@receiver(post_delete, sender=Employee)
def delete_user(sender, instance, **kwargs):
    # Создание пользователя с такими же данными как у работника
    try:
        u = User.objects.get(username = instance.user_name)
        u.delete()
    except:
        raise Http404('Cant find user with such username')

class SeasonListFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = ("season")

    # Parameter for the filter that will be used in the URL query.
    parameter_name = "date"

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return [
            ("summer", ("summer")),
            ("autumn", ("autumn")),
            ("winter", ("winter")),
            ("spring", ("spring")),
        ]

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        # Compare the requested value (summer, autumn, sping, winter)
        # to decide how to filter the queryset.
        if self.value() == "summer":
            return queryset.filter(
                date__month__in=range(6,9),
            )
        if self.value() == "autumn":
            return queryset.filter(
                date__month__in=range(9,12),
            )
        if self.value() == "winter":
            return queryset.filter(
                date__month__in=(12,1,2)
            )
        if self.value() == "spring":
            return queryset.filter(
                date__month__in=range(3,6),
            )
        
class HalfYearListFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = ("6 months")

    # Parameter for the filter that will be used in the URL query.
    parameter_name = "date"

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return [
            ("half_year", ("6 months")),
        ]

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        # Compare the requested value (summer, autumn, sping, winter)
        # to decide how to filter the queryset.
        if self.value() == "half_year":
            return queryset.filter(
                admission_date__gte=datetime.now() - timedelta(weeks=25.86),
                admission_date__lte=datetime.now(),
            )



@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    pass

@admin.register(Exposition)
class ExpositionAdmin(admin.ModelAdmin):
    pass

@admin.register(Exhibition)
class ExhibitionAdmin(admin.ModelAdmin):
    pass


@admin.register(Exhibit)
class ExhibitAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_art_form', 'admission_date', 'observer',)

    list_filter = [HalfYearListFilter]

    form = ExhibitForm

@admin.register(Hall)
class HallAdmin(admin.ModelAdmin):
    list_display = ('number', 'name', 'floor', 'area', 'display_exhibits_count', 'display_exhibit')

    search_fields=['exhibit__admission_date']

    date = datetime(1,1,1)

    # displays exhibits count, which admission_date greather then entered date
    def display_exhibits_count(self, obj):
        return self.model.objects.filter(exhibit__admission_date__gte=self.date, name = obj).count()

    # sets entered date to self.date, in the purpose of getting count
    def get_search_results(self, request, queryset, search_term):

        # this patter gets year, moth, day from user
        # search term
        pattern = r".*(\d{4}).*(\d{2}).*(\d{2}).*"

        matches = re.search(pattern, search_term)
        if matches:
            year = matches.group(1)
            month = matches.group(2)
            day = matches.group(3)
            self.date = datetime(int(year), int(month),int(day))

        return self.model.objects, True
    
    def display_exhibit(self, obj):
        return ', '.join([ exhibit.name for exhibit in obj.exhibit.filter(admission_date__gte=self.date)[:3] ])
        


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('user_name','first_name', 'last_name', 'hall', 'phone_number', 'position')

    search_fields = ['hall__floor']

@admin.register(ArtForm)
class ArtFormAdmin(admin.ModelAdmin):
    pass

@admin.register(Excursion)
class ExcursionAdmin(admin.ModelAdmin):
    list_filter = [SeasonListFilter]

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    pass


