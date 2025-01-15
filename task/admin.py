from django.contrib import admin
from .models import Task,TaskComment
from djangoql.admin import DjangoQLSearchMixin

# Register your models here.
@admin.register(Task)
class TaskAdmin(DjangoQLSearchMixin,admin.ModelAdmin):
    list_display=['name','priority','project','duration','assigned_to','start_date','end_date']

@admin.register(TaskComment)
class TaskCommentAdmin(DjangoQLSearchMixin,admin.ModelAdmin):
    list_display=['user','task','comment']


