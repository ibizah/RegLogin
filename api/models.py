from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserModel(models.Model):
    #user= models.OneToOneField(User, on_delete=models.CASCADE)
    email= models.EmailField()
    username=models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    zipcode= models.IntegerField()

    def __str__(self):
        return self.username
