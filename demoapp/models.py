from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Employee(models.Model):
    fname= models.CharField(max_length=200)
    email = models.EmailField()
    age= models.IntegerField()

    def __str__(self):
        return self.fname




 #**********************************************************************#


class UserProfileInfo(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic =models.ImageField(upload_to='media', blank=True)
    profile_url= models.URLField(blank=True)

    def __str__(self):
        return self.user.username


#**************************************************************************

class Reg(models.Model):
    user= models.OneToOneField(User,on_delete=False)

    def __str__(self):
        return self.user.username
