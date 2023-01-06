from rest_framework.decorators import api_view, permission_classes
from user_app.api.serializers import RegistrationSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from student_app.models import Student
from student_app.api.serializers import StudentSerializer
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

@api_view(['POST'])
def logout_view(request):
    if request.method=='POST':
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
@api_view(['POST'])
def registration_view(request):
    if request.method=='POST':
        serializer= RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            account=serializer.save()
            refresh = RefreshToken.for_user(account)
            return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            })
            #return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])

def create_student(request):
    if request.method=='POST':
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        