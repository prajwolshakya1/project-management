from django.urls import path
from .views import project_index,ProjectAdd,ProjectDelete,ProjectUpdate

urlpatterns = [
    path('list',project_index,name='project-index'),
    path('project/add',ProjectAdd.as_view(),name='project_add'),
    path('update/<int:pk>',ProjectUpdate.as_view(),name="project_update"),
    path('delete/<int:pk>',ProjectDelete.as_view(),name="project_delete"),
]