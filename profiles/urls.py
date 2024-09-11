from django.urls import path, include
from profiles import views

urlpatterns = [
    path('cadastro', views.cadastro, name = 'cadastro'),
    path('login', views.login, name = 'login'),
    path('listausuarios', views.listausuarios, name = 'listausuarios'),
    path('app/', include('app.urls')),
    path('logout', views.logout, name = 'logout')
]