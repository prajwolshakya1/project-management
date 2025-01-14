from rest_framework.response import Response
from task.models import Task
from .serializers import TaskSerializer
from rest_framework.generics import GenericAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
class TaskView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        data = Task.objects.all()
        serializer = TaskSerializer(data, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        data = request.data
        serialzier = TaskSerializer(data=data)
        if serialzier.is_valid():
            serialzier.save()
            return Response({
                "message":"Project Added Successfully"
            })
        return Response(serialzier.errors)
    
class TaskRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
