from django.db import models

# Create your models here.

class Student_data(models.Model):
    name = models.CharField(max_length=100)
    std = models.CharField(max_length=100)
    bio = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
    
