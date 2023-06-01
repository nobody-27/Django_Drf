from django.db import models

# Create your models here.


class Token(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    bio = models.CharField(max_length=100)

    def __str__(self) -> str:
        return super().__str__()
    



