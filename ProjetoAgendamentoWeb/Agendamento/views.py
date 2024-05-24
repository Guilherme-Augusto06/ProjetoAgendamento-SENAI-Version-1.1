from django.shortcuts import render
from .models import Senai
from .forms import  formCadastroUsuario, FormLogin
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.conf import settings
from django.shortcuts import redirect

def homepage(request):
    context = {}
    dadosSenai = Senai.objects.all()
    context["dadosSenai"] = dadosSenai
    return render(request, 'homepage.html', context)

def homepageAdmin(request):
    context = {}
    dadosSenai = Senai.objects.all()
    context["dadosSenai"] = dadosSenai
    return render(request, 'homepageAdmin.html', context)


def cadastroUsuario(request):
    context = {}
    dadosSenai = Senai.objects.all()
    context["dadosSenai"] = dadosSenai
    if request.method == 'POST':
        form = formCadastroUsuario(request.POST)
        if form.is_valid():
            var_nome = form.cleaned_data['first_name']
            var_sobrenome = form.cleaned_data['last_name']
            var_usuario = form.cleaned_data['user']
            var_email = form.cleaned_data['email']
            var_senha = form.cleaned_data['password']

            user = User.objects.create_user(username=var_usuario, email=var_email, password=var_senha)
            user.first_name = var_nome
            user.last_name = var_sobrenome
            user.save()
            return redirect('/login')
    else:
        form = formCadastroUsuario()
        context['form'] = form
    return render(request, 'cadastroUsuario.html', context)

def login(request):
    context = {}
    dadosSenai = Senai.objects.all()
    context["dadosSenai"] = dadosSenai
    if request.method == 'POST':
        form = FormLogin(request.POST)
        if form.is_valid():
            var_usuario = form.cleaned_data['user']
            var_senha = form.cleaned_data['password']
            
            user = authenticate(username=var_usuario, password=var_senha)

            if user is not None:
                auth_login(request, user)
                return redirect('/homepageAdmin')
            else:
                print('Login falhou')
    else:
        form = FormLogin()
        context['form'] = form
    return render(request, 'login.html', context)
