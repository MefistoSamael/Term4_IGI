from datetime import date
from django.contrib import admin
from .models import ArtForm, Employee, Excursion, Exhibit, Exhibition, Exposition, Hall, Position, Theme


# admin.site.register(Theme)
# admin.site.register(Exposition)
# admin.site.register(Exhibition)
# admin.site.register(Exhibit)
# admin.site.register(Hall)
# admin.site.register(Employee)
# admin.site.register(ArtForm)
# admin.site.register(Excursion)
# admin.site.register(Position)

class SeasonListFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = ("season")

    # Parameter for the filter that will be used in the URL query.
    parameter_name = "admission_date"

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
                admission_date__month__in=range(6,9),
            )
        if self.value() == "autumn":
            return queryset.filter(
                admission_date__month__in=range(9,12),
            )
        if self.value() == "winter":
            return queryset.filter(
                admission_date__month__in=(12,1,2)
            )
        if self.value() == "spring":
            return queryset.filter(
                admission_date__month__in=range(3,6),
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
    list_display = ('name', 'display_art_form', 'admission_date', 'observer')

    list_filter = [SeasonListFilter]

@admin.register(Hall)
class HallAdmin(admin.ModelAdmin):
    list_display = ('number', 'name', 'floor', 'area')

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'hall', 'phone_number', 'position')

    search_fields = ['hall__floor']

@admin.register(ArtForm)
class ArtFormAdmin(admin.ModelAdmin):
    pass

@admin.register(Excursion)
class ExcursionAdmin(admin.ModelAdmin):
    pass

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    pass

