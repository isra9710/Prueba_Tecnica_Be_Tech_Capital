from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length = 30, unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True, unique=True)
    sex = models.CharField(max_length=8, blank=True, null=True)
    profile_picture = models.ImageField(default="default-profile.png",null=False, blank=False)
    