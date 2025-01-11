from django.shortcuts import render
from .models import Project

# Create your views here.
def project_index(request):
    projects=Project.objects.all()
    return render(request,'project/index.html',{'projects':projects})