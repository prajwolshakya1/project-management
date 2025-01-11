from rest_framework import serializers
from user.models import Department,Designation,EmployeeProfile
from user.models import Department,Designation
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        exclude =['password','groups','user_permissions']

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Department
        fields='__all__'




# class DesignationSerializer(serializers.ModelSerializer):
#     department=DepartmentSerializer()
#     class Meta:
#         model=Designation
#         fields='__all__'

class DesignationSerializer(serializers.ModelSerializer):
    department=DepartmentSerializer(read_only=True)
    class Meta:
        model=Designation
        fields='__all__'


    def to_representation(self,instance):
        data=super().to_representation(instance)
        data['department']=instance.department.name
        return data
    
class EmployeeProfileSerializer(serializers.ModelSerializer):
    designation=DesignationSerializer(read_only=True)
    user=UserSerializer(read_only=True)
    class Meta:
        model=EmployeeProfile
        exclude=['salary']

class DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Designation
        fields='__all__'


    def to_representation(self,instance):
        data=super().to_representation(instance)
        data['department']=instance.department.name
        return data




