from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class user_details(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    # phone=models.CharField(max_length=15)
    # qualification=models.CharField(max_length=20)

def __str__(self):
    return str(self.user.username.__str__())