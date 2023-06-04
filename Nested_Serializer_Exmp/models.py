from django.db import models

# Create your models here.

class common(models.Model):  # COMM0N
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
  
    class Meta:
        abstract = True

class Profile(common):
    display_name = models.CharField(max_length=30)
    mobile = models.IntegerField()
    address = models.TextField()
    email = models.EmailField()
    dob = models.DateField()
    photo=models.FileField(upload_to='profile_data/',null=True,blank=True)
    status = models.IntegerField(default=1)
    

    def __str__(self) -> str:
        return self.display_name



class Hobby(common):   
    user=models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='user_hobby',null=True,blank=True)
    name = models.CharField(max_length=30)
    description = models.TextField()
    status = models.IntegerField(default=1)