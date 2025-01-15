from user.models import Department,Designation,EmployeeProfile
from .serializers import ProjectSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from project.models import Project,ProjectRole
from .serializers import ProjectSerializer,ProjectRoleSerializer
from rest_framework.views import APIView,View
from rest_framework.generics import GenericAPIView,RetrieveDestroyAPIView,RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle,AnonRateThrottle

@api_view(['GET'])
def project_list(request):
    data=Project.objects.all()
    serializer=ProjectSerializer(data,many=True)
    return Response(serializer.data)


class ProjectView(APIView):
    permission_classes=[IsAuthenticated]
    throttle_classes=[UserRateThrottle,AnonRateThrottle]
    def get(self,request):
        data=Project.objects.all()
        serializer=ProjectSerializer(data,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        data=request.data
        serializer=ProjectSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Project added"})
        return Response(serializer.errors)
    
    # serializer.save(raise_exception=True)


# @api_view(['POST'])
# def add_department(request):
#     data=request.data
#     serializer=DepartmentSerializer(data=data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response('')
#     return Response(serializer.errors)

class ProjectRetrieveDestroyView(RetrieveDestroyAPIView):
    queryset=Project.objects.all()
    serializer_class=ProjectSerializer

class ProjectRoleView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request):
        data=ProjectRole.objects.all()
        serializer=ProjectRoleSerializer(data,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        data=request.data
        serializer=ProjectSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Project added Successfully"})
        return Response(serializer.errors)

class ProjectRoleRetrieveDestroyView(RetrieveUpdateAPIView):
    queryset=ProjectRole.objects.all()
    serializer_class=ProjectRoleSerializer
