from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Department(models.Model):
    name=models.CharField(max_length=100)
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Designation(models.Model):
    department=models.ForeignKey(Department,on_delete=models.RESTRICT)
    name=models.CharField(max_length=100)
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.name
    


class EmployeeProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    address=models.CharField(max_length=100)
    phone_number=models.BigIntegerField(default=0)
    joining_date=models.DateField()
    years_of_experience=models.IntegerField(default=0)
    designation=models.ForeignKey(Designation,on_delete=models.RESTRICT)
    salary=models.IntegerField(default=0)
    is_active=models.BooleanField(default=True)
    end_date=models.DateField(null=True,blank=True)
