from django.contrib import admin
from .models import Task
from djangoql.admin import DjangoQLSearchMixin

# Register your models here.
@admin.register(Task)
class TaskAdmin(DjangoQLSearchMixin,admin.ModelAdmin):
    list_display=['name','priority','project','duration','assigned_to','start_date','end_date']