from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
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
        assigned_to_username = request.POST.get('assigned_to')
        assigned_to = User.objects.filter(username=assigned_to_username).first()
        task = Task.objects.create(task_name=task_name, task_desc=task_desc, assigned_to=assigned_to)
        task.save()

        return HttpResponse('Tarefa criada com sucesso') 

@login_required
def my_tasks(request):
    all_tasks = Task.objects.filter(assigned_to=request.user)
    return render(request, 'my_tasks.html', {'tarefas': all_tasks})

@login_required
def my_tasks_filter(request, status):
    show_tasks = Task.objects.filter(assigned_to=request.user, task_status=status)
    return render(request, 'my_tasks.html', {'tarefas': show_tasks})

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
            
            return HttpResponse('Tarefa modificada com sucesso') 
        
@login_required
def delete_task(request, id):
    task = get_object_or_404(Task, id=id).delete()
    return HttpResponse('Tarefa deletada com sucesso') 

        