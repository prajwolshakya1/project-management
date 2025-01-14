from django.shortcuts import render
from .models import Department,Designation,EmployeeProfile
from django.views.generic import UpdateView,DeleteView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
def department_list(request):
    departments = Department.objects.all()
    return render(request, 'department/department_list.html', {'departments': departments})

class DepartmentAdd(LoginRequiredMixin,CreateView):
    model=Department
    template_name="department/department_create.html"
    fields="__all__"
    success_url="/user/department/list"

class DepartmentUpdate(LoginRequiredMixin,UpdateView):
    model=Department
    template_name="department/department_update.html"
    fields="__all__"
    success_url="/user/department/list"

class DepartmentDelete(LoginRequiredMixin,DeleteView):
    model=Department
    template_name="department/department_delete.html"
    success_url="/user/department/list"

def designation_list(request):
    designations =Designation.objects.all()
    return render(request,'designation/designation_list.html',{'designations':designations})

class DesignationAdd(LoginRequiredMixin,CreateView):
    model=Designation
    template_name='designation/designation_create.html'
    fields='__all__'
    success_url="/user/designation/list"

class DesignationUpdate(LoginRequiredMixin,UpdateView):
    model=Designation
    template_name='designation/designation_update.html'
    fields='__all__'
    success_url='/user/designation/list'

class DesignationDelete(LoginRequiredMixin,DeleteView):
    model=Designation
    template_name='designation/designation_delete.html'
    success_url='/user/designation/list'

def employee_list(request):
    employees =EmployeeProfile.objects.all()
    return render(request,'employeeprofile/employee_list.html',{'employees':employees})

class EmployeeAdd(LoginRequiredMixin,CreateView):
    model=EmployeeProfile
    fields="__all__"
    template_name='employeeprofile/employee_create.html'
    success_url='/user/employee/list'

class EmployeeUpdate(LoginRequiredMixin,UpdateView):
    model=EmployeeProfile
    fields="__all__"
    template_name='employeeprofile/employee_update.html'
    success_url="/user/employee/list"

class EmployeeDelete(LoginRequiredMixin,DeleteView):
    model=EmployeeProfile
    template_name="employeeprofile/employee_delete.html"
    success_url="/user/employee/list"