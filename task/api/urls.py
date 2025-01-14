from django.urls import path, include
from .views import TaskView,TaskRetrieveUpdateDestroyView
urlpatterns = [
    path('list',TaskView.as_view(), name="task-list-api"),
    path('list/<int:pk>',TaskRetrieveUpdateDestroyView.as_view(), name="task-update-retrieve-destroy-api"),
    
  
]