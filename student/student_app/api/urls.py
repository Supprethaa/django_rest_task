from django.urls import path,include
from student_app.api.views import student_list,student_details

urlpatterns = [
    
    path('list/',student_list,name='stud-list'),
    path('<int:pk>',student_details,name='stud-details'),
    
]