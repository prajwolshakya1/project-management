from django.urls import path,include
from .views import project_list,ProjectView,ProjectRetrieveDestroyView,ProjectRoleView,ProjectRoleRetrieveDestroyView


urlpatterns = [
    
    path('',project_list,name="project-list-api"),
    path('class/project',ProjectView.as_view(),name="project-list-api"),
    path('class/project/<int:pk>',ProjectRetrieveDestroyView.as_view(),  name="project-retrieve-destroy-api"),
    path('class/project',ProjectRoleView.as_view(), name="project_role-list-api"),
    path('class/project/<int:pk>',ProjectRoleRetrieveDestroyView.as_view(),name="project_role-retrieve-destroy-api"),
   
   




]