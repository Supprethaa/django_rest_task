from django.shortcuts import render
from student_app.models import Student
from django.http import JsonResponse
# Create your views here.

def student_list(request):
    students=Student.objects.all()
    data={'students':list(students.values())}
    
    return JsonResponse(data)

def student_details(request,pk):
    student=Student.objects.get(pk=pk)
    data={
        'Name':student.name,
        'Age':student.age,
        'Position':student.position
        
    }
    return JsonResponse(data)
    