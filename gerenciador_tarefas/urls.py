from profiles import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),    
    path('', views.login, name='login'),
    path('profiles/', include('profiles.urls')),
    path('app/', include('app.urls'))
]
