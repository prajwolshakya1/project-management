from django.contrib import admin
from djangoql.admin import DjangoQLSearchMixin
from .models import *

# Register your models here.
@admin.register(EmployeeProfile)
class EmployeeProfileAdmin(DjangoQLSearchMixin,admin.ModelAdmin):
    list_display=['user','designation','is_active']

@admin.register(Department)
class DepartmentAdmin(DjangoQLSearchMixin,admin.ModelAdmin):
    pass

@admin.register(Designation)
class DesignationAdmin(DjangoQLSearchMixin,admin.ModelAdmin):
    pass

