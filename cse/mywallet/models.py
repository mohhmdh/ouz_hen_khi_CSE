from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class wallet(models.Model) :
     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
     money = models.PositiveIntegerField(default=0)
     allmoney =  models.PositiveIntegerField(default=0)
     name = models.CharField(max_length=20)
     
