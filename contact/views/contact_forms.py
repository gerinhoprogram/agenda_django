from django.shortcuts import render, redirect
from contact.models import Contact
from django.shortcuts import get_object_or_404, render
from django .db.models import Q

# https://docs.djangoproject.com/en/4.2/topics/pagination/
from django.core.paginator import Paginator

# Create your views here.

def create(request):
  
    context = {
    }

    return render(
        request,
        'contact/create.html',
        context
    )

