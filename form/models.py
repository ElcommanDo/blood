from django.db import models
from django.contrib.auth.models import User

class Doner(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=200)
    blood_type = models.CharField(max_length=10)
    city = models.CharField(max_length=50)
    type = models.CharField(max_length=50, default='None')

    def __str__(self):
        return self.user.username
