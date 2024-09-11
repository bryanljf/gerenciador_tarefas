from django.db import models
from django.contrib.auth.models import User

# Classe Tarefa, armazena todas as informações da tarefa criada pelo usuário

class Task(models.Model):   
    task_name = models.CharField(max_length=100, default='Nova Tarefa')
    task_desc = models.TextField(max_length=254, null=True)
    task_status = models.TextField(max_length=12, default='Pendente')
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
