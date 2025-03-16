from django.db import models

# Create your models here.
class card(models.Model) :
    card_n=models.IntegerField(default=0)
    e_date =models.CharField(max_length=20)
    cvv=models.CharField(max_length=20)
