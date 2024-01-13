# from django.shortcuts import render, redirect
from contact.models import Contact
from django.shortcuts import render
from contact.forms import ContactForm

# https://docs.djangoproject.com/en/4.2/topics/pagination/
from django.core.paginator import Paginator

# Create your views here.

def create(request):

    # se o formulario é enviado       
    if request.method == 'POST':
        context = {
            'form': ContactForm(request.POST)
        }

        return render(
            request,
            'contact/create.html',
            context
        )
  
    # leva para a view o ContactForm com os inputs
    context = {
        'form': ContactForm()
    }

    return render(
        request,
        'contact/create.html',
        context
    )

