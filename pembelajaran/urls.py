from django.urls import path
from . import views

app_name = 'pembelajaran'

urlpatterns = [
    # Auth URLs
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Public URL
    path('', views.index, name='index'),

    # Protected URLs
    path('about-us/', views.aboutus, name='aboutus'),
    path('belajar-cli/', views.linux_dasar, name='belajar_cli'),
    path('kamus-cli/', views.belajar_linux, name='kamus_cli'),
    path('install-linux/', views.install_linux, name='install_linux'),

    # Chapters
    path('belajar-cli/chapter1/', views.linux_chapter1, name='linux_chapter1'),
    path('belajar-cli/chapter2/', views.linux_chapter2, name='linux_chapter2'),
    path('belajar-cli/chapter3/', views.linux_chapter3, name='linux_chapter3'),
]