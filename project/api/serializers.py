from rest_framework import serializers
from django.contrib.auth.models import User
from project.models import Project


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Project
        fields='__all__'

    def to_representation(self,instance):
        data=super().to_representation(instance)
        data['start_date']=instance.start_date if instance.start_date else ""
        data['end_date']=instance.end_date if instance.end_date else ""
        data['deadline']=instance.deadline if instance.deadline else ""
        return data




