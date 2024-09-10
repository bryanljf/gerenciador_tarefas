from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

# class Users(models.Model):
#     username = models.TextField(max_length=20, unique=True)
#     password = models.TextField(max_length=8)
#     email = models.EmailField(max_length=254, unique=True)