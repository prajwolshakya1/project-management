from django.db import models
from project.models import Project
from user.models import EmployeeProfile

# Create your models here.
class Task(models.Model):
    class TaskStatus(models.TextChoices):
        Highest_priority="Highest_Priority"
        Lowest_priority="Lowest_Priority"
    name=models.CharField(max_length=50)
    priority=models.CharField(max_length=20,choices=TaskStatus.choices)
    project=models.ForeignKey(Project,on_delete=models.RESTRICT)
    duration=models.DurationField(null=True,blank=True)
    assigned_to=models.ForeignKey(EmployeeProfile,on_delete=models.RESTRICT)
    start_date=models.DateTimeField(null=True,blank=True)
    end_date=models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.name




