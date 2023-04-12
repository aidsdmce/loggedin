from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rollno = models.CharField(max_length=100)
    studentid = models.CharField(max_length=20)
