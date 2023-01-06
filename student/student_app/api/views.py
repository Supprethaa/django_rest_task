from student_app.models import Student
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from student_app.api.serializers import StudentSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser

@api_view(['GET','POST'])
@permission_classes([IsAdminUser])
def student_list(request):
    if request.method== 'GET':
        
            
        student=Student.objects.all()
        
        serializer=StudentSerializer(student,many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

        
@api_view(['GET','POST','PUT','DELETE'])
@permission_classes([IsAdminUser,IsAuthenticated])
def student_details(request,pk):
    if request.method=='GET':
        try:

            student=Student.objects.get(pk=pk,name=request.user)
        except Student.DoesNotExist:
            return Response({'Error':'Student does not exist'},status=status.HTTP_404_NOT_FOUND)

        serializer=StudentSerializer(student)
        return Response(serializer.data)
    # if request.method == 'POST':
    #     serializer=StudentSerializer(data=request.data)
    #     if serializer.is_valid()  and serializer.:
    #         serializer.save()
    #         return Response(serializer.data)
    #     else:
    #         return Response(serializer.errors)
    if request.method=='PUT':
        student=Student.objects.get(pk=pk,name=request.user)

        serializer=StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    if request.method=='DELETE':
        student=Student.objects.get(pk=pk,name=request.user)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)