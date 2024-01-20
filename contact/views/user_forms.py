from django.shortcuts import render, redirect

# imorta as classes de contact/form.py
from contact.forms import RegisterForm, RegisterUpdateForm
from django.contrib import messages, auth
from django.contrib.auth.forms import AuthenticationForm


# formulário de registro
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

# renderiza a tela de login
def login_view(request):
    form = AuthenticationForm(request)

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            user = form.get_user()

            # faz o login do usuario
            auth.login(request, user)
            messages.success(request, 'Logado com sucesso')
            return redirect('contact:index')
        messages.error(request, 'Login inválido')

    return render(
        request,
        'contact/login.html',
        {
            'form':form
        }
    )


# faz logout
def logout_view(request):
    auth.logout(request)
    return redirect('contact:login')

def user_update(request):

    form = RegisterUpdateForm(instance=request.user)

    if request.method != 'POST':
        return render(
            request,
            'contact/register.html',
            {
                'form': form
            }
        )
    
    form = RegisterUpdateForm(data=request.POST, instance=request.user)

    if not form.is_valid():
        return render(
            request,
            'contact/register.html',
            {
                'form': form
            }
        )

    return render(
        request,
        'contact/register.html',
        {
            'form': form
        }
    )