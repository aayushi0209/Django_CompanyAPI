from django.contrib import admin
from .views import Company, Employee


# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'type')


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'company')


admin.site.register(Company, CompanyAdmin)
admin.site.register(Employee, EmployeeAdmin)
