from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    Country=models.CharField(max_length=50)
    State=models.CharField(max_length=50)
    #Destination= models.CharField(max_length=50)

    def __str__(self):
        return self.user.username


