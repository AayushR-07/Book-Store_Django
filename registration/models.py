from django.db import models

# Create your models here.

class Registration(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.name}"
    
