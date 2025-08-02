from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from taxi.models import Driver, Manufacture, Car

admin.site.register(Driver)
admin.site.register(Manufacture)
admin.site.register(Car)

@admin.register(Driver)
class DriverAdmin(UserAdmin):
    model = Driver

    fieldsets = UserAdmin.fieldsets + (
        ('Additional info', {'fields': ('license_number',)}),
    )

    list_display = UserAdmin.list_display + ('license_number',)