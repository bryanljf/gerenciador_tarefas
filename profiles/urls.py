from django.urls import path, include
from profiles import views

urlpatterns = [
    path('signup', views.signup, name = 'signup'),
    path('login', views.login, name = 'login'),
    path('user_list', views.user_list, name = 'user_list'),
    path('app/', include('app.urls')),
    path('logout', views.logout, name = 'logout')
]