import email
from django.db import models

# Create your models here.
class user(models.Model):
    name=models.CharField(max_length=70)
    email=models.EmailField()
    password=models.CharField(max_length=20)

    def __str__(self):
        return self.name