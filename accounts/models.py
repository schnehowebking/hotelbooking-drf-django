from django.db import models
from django.contrib.auth.models import User
# Create your models here.

GENDER = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    
]
class Customer(models.Model):
    user = models.OneToOneField(User, related_name = "customer", on_delete = models.CASCADE)
    image = models.ImageField(upload_to=f"accounts/images/")
    acc_balance = models.DecimalField(max_digits=12, decimal_places=2, default = 0.00)
    gender = models.CharField(choices = GENDER, max_length = 10)
    mobile_no = models.CharField(max_length = 12)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"