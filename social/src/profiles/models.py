from distutils.command.upload import upload
import email
from email.policy import default
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    first_name = models.CharField(max_length=200 , blank=True)
    last_name  = models.CharField(max_length=200 , blank=True)
    user       = models.OneToOneField(User , on_delete=models.CASCADE)
    email      = models.EmailField(max_length=200 , blank=True) 
    avatar     = models.ImageField(default = 'avatar.png' , upload_to='avatars/')
    updated    = models.DateTimeField(auto_now= True)
    created    = models.DateTimeField(auto_now_add=True)
    admin      = models.BooleanField()
    

    def __str__(self):
        return f"{self.user.username}-{self.created}"