from django.db import models

class User(models.Model):
    username = models.TextField(max_length=20)
    password = models.TextField(max_length=8)
    email = models.EmailField(max_length=254)
