from django.db import models
from django.contrib.auth.models import User

class card(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    card_n = models.CharField(max_length=16)  
    e_date = models.CharField(max_length=7)
    cvv = models.CharField(max_length=3)  

    def __str__(self):
        return f"Card ending in {self.card_n[-4:]}"  # Displaying last 4 digits of card number for security
