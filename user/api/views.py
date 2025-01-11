from user.models import Department,Designation,EmployeeProfile
from .serializers import DepartmentSerializer,DesignationSerializer,EmployeeProfileSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import authentication_classes,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView,View
from rest_framework.generics import GenericAPIView



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def department_list(request):
    data=Department.objects.all()
    serializer=DepartmentSerializer(data,many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def designation_list(request):
    data=Designation.objects.all()
    serializer=DesignationSerializer(data,many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def employee_list(request):
    data=EmployeeProfile.objects.filter(is_active=True)
    serializer=EmployeeProfileSerializer(data,many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def employee_datail(request,pk):
    data=EmployeeProfile.objects.get(pk=pk)
    serializer=EmployeeProfileSerializer(data)
    return Response(serializer.data)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_department(request):
    data=request.data
    serializer=DepartmentSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            "message":"department added successfully"
        })
    return Response(serializer.errors)

@api_view(['POST'])
def add_designation(request):
    data=request.data
    serializer=DesignationSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            "message":"designation added successfully"
        })
    return Response(serializer.errors)

class EmployeeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = EmployeeProfile.objects.filter(is_active=True)
        serializer = EmployeeProfileSerializer(data, many=True)
        return Response({
            "status":True,
            "data":serializer.data
        })

    def post(self, request):
        data = request.data
        serializer = EmployeeProfileSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    

class DepartmentUpdateAndDeleteView(APIView):
    def put(self, request, pk):
        data = Department.objects.get(id=pk)
        request_data = request.data
        serializer = DepartmentSerializer(data=request_data, instance=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk):
        data = Department.objects.get(id=pk)
        data.delete()
        return Response({"message": "Department deleted successfully"})    