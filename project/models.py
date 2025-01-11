from django.db import models

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