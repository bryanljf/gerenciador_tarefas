from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Task

def home(request):
    return render(request, 'home.html')

@login_required
def create_task(request):
    if request.method == "GET":
        all_users = User.objects.all()
        return render(request, 'create_task.html', {'usuarios': all_users})
    else:
        task_name = request.POST.get('task_name')
        task_desc = request.POST.get('task_desc')
        #task_status = request.POST.get('task_status')
        assigned_to_username = request.POST.get('assigned_to')
        assigned_to = User.objects.filter(username=assigned_to_username).first()
        task = Task.objects.create(task_name=task_name, task_desc=task_desc, assigned_to=assigned_to)
        task.save()

        return HttpResponse('Tarefa criada com sucesso') 
        
@login_required
def my_tasks(request):
    all_tasks = Task.objects.all()
    return render(request, 'my_tasks.html', {'tarefas': all_tasks})
        