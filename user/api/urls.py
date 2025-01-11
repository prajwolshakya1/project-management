from django.urls import path,include
from .views import (department_list,designation_list,employee_list,employee_datail,add_department,add_designation)

urlpatterns = [
    
    path('department',department_list,name="department-list-api"),
    path('designation',designation_list,name="designation-list-api"),
    path('employee',employee_list,name="employee-list-api"),
    path('employee/<int:pk>',employee_datail,name="employee-detail-api"),
    path('department/add',add_department,name="add-department-api"),
    path('designation/add',add_designation,name="add-designation-api"),






]