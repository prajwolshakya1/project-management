from django.db import models
from project.models import Project
from user.models import EmployeeProfile

# Create your models here.
class Task(models.Model):
    class TaskPriority(models.TextChoices):
        Highest_priority="Highest_Priority"
        Lowest_priority="Lowest_Priority"

    class TaskStatus(models.TextChoices):
        TODO='TODO'
        IN_PROGRESS='IN PROGRESS'
        IN_REVIEW='IN REVIEW'
        DONE='DONE'

    name=models.CharField(max_length=50)
    priority=models.CharField(max_length=20,choices=TaskPriority.choices,null=True,blank=True)
    status=models.CharField(max_length=20,choices=TaskStatus.choices,default=TaskStatus.TODO)
    project=models.ForeignKey(Project,on_delete=models.RESTRICT)
    duration=models.DurationField(null=True,blank=True)
    assigned_to=models.ForeignKey(EmployeeProfile,on_delete=models.RESTRICT)
    start_date=models.DateTimeField(null=True,blank=True)
    end_date=models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.name

class TaskComment(models.Model):
    task=models.ForeignKey(Task,on_delete=models.RESTRICT)
    user=models.ForeignKey(EmployeeProfile,on_delete=models.RESTRICT)
    comment=models.CharField(max_length=100)

    def __str__(self):
        return f'{self.task}-{self.user}'


