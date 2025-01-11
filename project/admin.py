from django.contrib import admin
from .models import Project
from djangoql.admin import DjangoQLSearchMixin

# Register your models here.
@admin.register(Project)
class ProjectAdmin(DjangoQLSearchMixin, admin.ModelAdmin):
    pass