from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.

class Student(models.Model):
    #stud_user=models.ForeignKey(User, on_delete=models.CASCADE)
    #stud_user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    name=models.CharField(max_length=25)
    age=models.IntegerField()
    position=models.CharField(max_length=50)
    
    def _str_(self):
        return self.name
    

    
