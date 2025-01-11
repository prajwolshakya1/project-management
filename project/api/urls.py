from django.urls import path,include
from .views import project_list,ProjectView


urlpatterns = [
    
    path('',project_list,name="project-list-api"),
    path('class/project',ProjectView.as_view(),name="project-list-api"),

   




]