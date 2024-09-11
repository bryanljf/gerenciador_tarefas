from django.urls import path
from app import views

urlpatterns = [
    path('create_task', views.create_task, name='create_task'),
    path('home', views.home, name='home'),
    path('my_tasks', views.my_tasks, name='my_tasks'),
    path('my_tasks_filter/<str:status>', views.my_tasks_filter, name='my_tasks_filter'),
    path('manage_task/<int:id>/', views.manage_task, name='manage_task')
]