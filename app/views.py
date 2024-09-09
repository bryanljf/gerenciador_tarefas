from django.shortcuts import render
from .models import User

def home(request):
    return render(request, 'home.html')

def users(request):
    new_user = User()
    new_user.id = request.POST.get('id_user')
    new_user.mail = request.POST.get('mail')
    new_user.password = request.POST.get('password')
    new_user.save()
    users = {
        'users': User.objects.all()
    }
    return render(request, 'users.html', users)
