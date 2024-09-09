from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate,
from .models import User

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

        user = authenticate(username=username, password=password)

        if user:
            login_django
