from profiles import views
from django.contrib import admin
from django.urls import path, include

#ESTUDAR SE FAZ SENTIDO TODAS AS ROTAS DO PROJETO ESTAREM NESSE MODULO

urlpatterns = [
    path('admin/', admin.site.urls),    
    path('', views.login, name='login'),
    path('profiles/', include('profiles.urls')),
    path('app/', include('app.urls'))
]
