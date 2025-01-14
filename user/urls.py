from django.urls import path, include
from .views import (department_list,
                    designation_list,
                    employee_list,
                    DepartmentAdd,
                    DepartmentUpdate,
                    DepartmentDelete,
                    DesignationAdd,
                    DesignationUpdate,
                    DesignationDelete,
                    EmployeeAdd,
                    EmployeeUpdate,
                    EmployeeDelete,
                    )

urlpatterns = [
    path('department/list',department_list,name="department_list"),
    path('designation/list',designation_list,name="designation_list"),
    path('employee/list',employee_list,name="employee_list"),
    path('department/add',DepartmentAdd.as_view(),name='department_add'),
    path('department/update/<int:pk>',DepartmentUpdate.as_view(),name='department_update'),
    path('department/delete/<int:pk>',DepartmentDelete.as_view(),name='department_delete'),
    path('designation/add',DesignationAdd.as_view(),name="designation_add"),
    path('designation/update/<int:pk>',DesignationUpdate.as_view(),name="designation_update"),
    path('designation/delete/<int:pk>',DesignationDelete.as_view(),name='designation_delete'),
    path('employee/add',EmployeeAdd.as_view(),name='employee_add'),
    path('employee/update/<int:pk>',EmployeeUpdate.as_view(),name="employee_update"),
    path('employee/delete/<int:pk>',EmployeeDelete.as_view(),name="employee_delete"),
]