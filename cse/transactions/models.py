from django.db import models
from django.contrib.auth.models import User

class transactions (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    transaction_id = models.CharField(max_length=20, unique=True)  # Use a unique ID
    name = models.CharField(max_length=100)
    date = models.DateField()
    status = models.CharField(max_length=20, choices=[
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Failed', 'Failed'),  # Add more statuses as needed
    ])
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.transaction_id} - {self.name} - {self.date}"