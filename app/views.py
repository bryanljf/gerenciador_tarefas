from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Task

# Render página home
def home(request):
    return render(request, 'home.html')

# Cria uma nova tarefa, conforme especificações do usuário
@login_required
def create_task(request):
    if request.method == "GET":
        all_users = User.objects.all()
        return render(request, 'create_task.html', {'usuarios': all_users})
    else:
        task_name = request.POST.get('task_name')
        task_desc = request.POST.get('task_desc')
        assigned_to_username = request.POST.get('assigned_to')
        assigned_to = User.objects.filter(username=assigned_to_username).first()
        task = Task.objects.create(task_name=task_name, task_desc=task_desc, assigned_to=assigned_to)
        task.save()

        return HttpResponse('Tarefa criada com sucesso') 

# Lista as tarefas do usuário logado, conforme a filtragem desejada
@login_required
def my_tasks(request):
            
    if request.method == "GET":
        all_tasks = Task.objects.filter(assigned_to=request.user)

        return render(request, 'my_tasks.html', {'tarefas': all_tasks})
    else:
        status = request.POST.get('status_filter')
        show_tasks = Task.objects.filter(assigned_to=request.user, task_status=status)
        return render(request, 'my_tasks.html', {'tarefas': show_tasks, 'selected_status': status})

# Gerenciamento da tarefa, permitindo a edição dos campos 
@login_required
def manage_task(request, id):
        if request.method == "GET":
            task = get_object_or_404(Task, id=id)
            all_users = User.objects.all()
            return render(request, 'manage_task.html', {'edit_task': task, 'usuarios': all_users})
        else:
            task_name = request.POST.get('task_name')
            task_desc = request.POST.get('task_desc')
            assigned_to_username = request.POST.get('assigned_to')
            assigned_to = User.objects.filter(username=assigned_to_username).first()
            task_status = request.POST.get('task_status')

            Task.objects.filter(id=id).update(task_name=task_name, task_desc=task_desc, task_status=task_status, assigned_to=assigned_to)
            
            all_tasks = Task.objects.filter(assigned_to=request.user)

            return render(request, 'my_tasks.html', {'tarefas': all_tasks})

# Deleta a tarefa 
@login_required
def delete_task(request, id):
    get_object_or_404(Task, id=id).delete()
    return redirect(reverse('my_tasks'))

# Lista todas as tarefas de usuários do sistema
@login_required
def all_tasks(request):
    if request.method == "GET":
        all_tasks = Task.objects.all()
        return render(request, 'all_tasks.html', {'tarefas': all_tasks})
    else:
        status = request.POST.get('status_filter')
        show_tasks = Task.objects.filter(task_status=status)
        return render(request, 'all_tasks.html', {'tarefas': show_tasks, 'selected_status': status})

        