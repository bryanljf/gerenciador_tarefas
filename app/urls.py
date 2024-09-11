from django.urls import path
from app import views

#Rotas utilizadas na aplicação 'app'

urlpatterns = [
    path('create_task', views.create_task, name='create_task'),
    path('home', views.home, name='home'),
    path('my_tasks', views.my_tasks, name='my_tasks'),
    path('manage_task/<int:id>/', views.manage_task, name='manage_task'),
    path('delete_task<int:id>/', views.delete_task, name='delete_task'),
    path('all_tasks', views.all_tasks, name='all_tasks')
]