from django.shortcuts import render
from .models import Project
from django.views.generic import UpdateView,DeleteView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ProjectForm

# Create your views here.
def project_index(request):
    projects = Project.objects.all()
    return render(request, 'project/index.html', {'projects': projects})

class ProjectAdd(LoginRequiredMixin,CreateView):
    model=Project
    form_class = ProjectForm
    template_name="project/project_create.html"
    success_url='/project/list'

class ProjectUpdate(LoginRequiredMixin,UpdateView):
    model=Project
    form_class = ProjectForm
    template_name='project/project_update.html'
    success_url="/project/list"

class ProjectDelete(LoginRequiredMixin,DeleteView):
    model=Project
    template_name='project/project_delete.html'
    success_url='/project/list'