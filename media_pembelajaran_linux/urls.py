from django.contrib import admin
from django.urls import path, include
from pembelajaran import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pembelajaran.urls')),
    path('install-linux/', views.install_linux, name='install_linux'),
]
