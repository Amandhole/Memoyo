from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from MemoyoApp.managers import MyCustomManager

class MyUser(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(max_length=300, unique=True)
    password = models.CharField(max_length=200,blank=True,null=True)
    is_staff = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] 

    objects = MyCustomManager()

    def __str__(self):
        return self.email

class UserDetails(models.Model):
    fk_myuser = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, null=True)
    profile_pic = models.FileField(upload_to="profiles/", blank=True, null=True)
    tagline = models.CharField(max_length=1000, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    tags = models.TextField(blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    reel = models.URLField(blank=True, null=True)
    looking_for_work = models.BooleanField(default=False)
    website = models.URLField(blank=True, null=True)
    
    social_1 = models.URLField(blank=True, null=True)
    social_2 = models.URLField(blank=True, null=True)
    social_3 = models.URLField(blank=True, null=True)