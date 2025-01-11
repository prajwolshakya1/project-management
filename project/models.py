from django.db import models
from django.contrib.auth.models import User
from user.models import EmployeeProfile

# Create your models here.
class Project(models.Model):
    class ProjectStatus(models.TextChoices):
        SUCCESS = "SUCCESS"
        IN_PROGRESS = "IN PROGRESS"
        ABORT = "ABORT"
        NOT_STARTED = "NOT STARTED"

    name = models.CharField(max_length=50)
    status = models.CharField(max_length=20,choices=ProjectStatus.choices,default=ProjectStatus.NOT_STARTED)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    deadline = models.DateTimeField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.name
    
class ProjectRole(models.Model):
    name=models.CharField(max_length=50)
    created_at=models.DateTimeField(auto_now=True)
    modified_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class ProjectMembership(models.Model):
    member=models.ForeignKey(EmployeeProfile,on_delete=models.CASCADE)
    role=models.ForeignKey(ProjectRole,on_delete=models.CASCADE)
    project=models.ForeignKey(Project,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now=True)
    modified_at=models.DateTimeField(auto_now_add=True)

class Meta:
    unique_together=['member','project']

def __str__(self):
    return f'{self.member}-{self.role}-{self.project}'