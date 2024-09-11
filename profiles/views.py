from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth import logout as logout_django
from django.contrib.auth.models import User

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else:
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username=username).first()
        mail = User.objects.filter(email=email).first()

        if user or mail:
            return HttpResponse('Esse username ou email já foi cadastrado anteriormente...')
    
    user = User.objects.create_user(username=username, email=email, password=password)
    user.save()

    return HttpResponse('Cadastro de usuário feito com sucesso!')

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login_django(request, user)
            return render(request, 'home.html')
        else:
            return HttpResponse('Username ou senha inválido!')
        
def listausuarios(request):
    all_users = User.objects.all()
    return render(request, 'listausuarios.html', {'usuarios': all_users})

def logout(request):
    logout_django(request)
    return redirect('login')


