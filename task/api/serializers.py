from rest_framework import serializers
from django.contrib.auth.models import User
from task.models import Task,TaskComment
from project.api.serializers import Project, ProjectSerializer
from user.api.serializers import EmployeeProfileSerializer
class TaskSerializer(serializers.ModelSerializer):
    project=ProjectSerializer(read_only=True)
    assigned_to=EmployeeProfileSerializer(read_only=True)
    taskcomment=serializers.SerializerMethodField()
    class Meta:
        model = Task
        fields = '__all__'
    def to_representation(self, instance):
        data=super().to_representation(instance)
        data['project']=instance.project.name
        data['duration']=instance.duration if instance.duration else ""
        data['start_date']=instance.start_date if instance.start_date else ""
        data['end_date']=instance.end_date if instance.end_date else ""
        data['assigned_to']=instance.assigned_to.user.username
        return data
    
    def get_taskcomment(self,obj):
        comments=TaskComment.objects.filter(task=obj)
        return TaskCommentSerializer(comments,many=True).data
    
class TaskCommentSerializer(serializers.ModelSerializer):
    comment=serializers.CharField(max_length=100,required=True)

    class Meta:
        model=TaskComment
        fields='__all__'