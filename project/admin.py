from django.contrib import admin
from .models import Project,ProjectRole, ProjectMembership
from djangoql.admin import DjangoQLSearchMixin

# Register your models here.
@admin.register(Project)
class ProjectAdmin(DjangoQLSearchMixin, admin.ModelAdmin):
    pass

@admin.register(ProjectRole)
class ProjectRoleAdmin(DjangoQLSearchMixin, admin.ModelAdmin):
    list_display = ['name', 'created_at', 'modified_at']

@admin.register(ProjectMembership)
class ProjectMembershipAdmin(DjangoQLSearchMixin, admin.ModelAdmin):
    list_display = ['member', 'role', 'project', 'created_at', 'modified_at']
    list_filter = ['role', 'project']