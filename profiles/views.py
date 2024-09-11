from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth import logout as logout_django
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Reponsável por cadastrar um novo usuário, fazendo a validação dos dados
def signup(request):
    if request.method == "GET":
        return render(request, 'signup.html')
    else:   
        min_len = 8
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username=username).first()
        mail = User.objects.filter(email=email).first()

        if user or mail:
            return HttpResponse('O usuário ou e-mail já foi cadastrado anteriormente...')

        elif len(password) < min_len:
            return HttpResponse('A senha deve ter no mínimo 8 carácteres...')
    
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()

            return render(request, 'login.html')

# Autentica o login, consultando se as credenciais são válidas
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

#Lista todos os usuários do sistema 
def user_list(request):
    all_users = User.objects.all()
    return render(request, 'user_list.html', {'usuarios': all_users})

#Logout do usuário
def logout(request):
    logout_django(request)
    return redirect('login')


