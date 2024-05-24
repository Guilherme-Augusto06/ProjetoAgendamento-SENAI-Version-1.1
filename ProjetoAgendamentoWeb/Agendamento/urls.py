from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name="home"),         # Inclui as urls do app blog
    path('cadastroUsuario', views.cadastroUsuario, name='cadastroUsuario'),
    path('login', views.login, name='login'),
    path('homepageAdmin', views.homepageAdmin, name='homepageAdmin'),
]