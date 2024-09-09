from django.db import models

class User(models.Model):
    id_user = models.AutoField(primary_key=True)
    mail = models.EmailField(max_length=250, null=True)
    password = models.TextField(max_length=200, null=True)

