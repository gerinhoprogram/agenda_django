from django.shortcuts import render, redirect
from contact.forms import RegisterForm
from django.contrib import messages, auth
from django.contrib.auth.forms import AuthenticationForm

def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()

            # mensagens 
            messages.info(request, 'Um texto')
            # messages.success(request, 'Um texto')
            # messages.warning(request, 'Um texto')
            # messages.error(request, 'Um texto')

            return redirect('contact:index')

    return render(
        request,
        'contact/register.html',
        {
            'form': form
        }
    )

def login_view(request):
    form = AuthenticationForm(request)

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            # messages.success(request, 'Logado com sucesso')

            # faz o login do usuario
            auth.login(request, user)
        else:
            messages.error(request, 'Login inválido')

    return render(
        request,
        'contact/login.html',
        {
            'form':form
        }
    )

def logout_view(request):
    auth.logout(request)
    return redirect('contact:login')