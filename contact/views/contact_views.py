from django.shortcuts import render, redirect
from contact.models import Contact
from django.shortcuts import get_object_or_404, render
from django .db.models import Q

# https://docs.djangoproject.com/en/4.2/topics/pagination/
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    contacts = Contact.objects.all().filter(show=True).order_by('-id')

    # mostra a query
    # print(contacts.query)

    paginator = Paginator(contacts, 10)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'site_title': 'Contatos - '
    }

    return render(
        request,
        'contact/index.html',
        context
    )

def contact(request, contact_id):

    #single_contact = Contact.objects.filter(pk=contact_id).first()
    single_contact = get_object_or_404(
        Contact, pk=contact_id, show=True
        )

    # mostra a query
    # print(contacts.query)
    contact_name = f'{single_contact.first_name} {single_contact.last_name}'

    context = {
        'contact': single_contact,
        'site_title': contact_name
    }

    return render(
        request,
        'contact/contact.html',
        context
    )

def search(request):

    search_value = request.GET.get('q', '').strip()

    if search_value == '':
        return redirect('contact:index')


    # filtro
    contacts = Contact.objects.all().filter(show=True).filter(Q(first_name__icontains=search_value) | Q(last_name__icontains=search_value)).order_by('-id')

    paginator = Paginator(contacts, 10)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    # mostra a query
    # print(contacts.query)

    #envia os dados para view 
    context = {
        'page_obj': page_obj,
        'site_title': 'Contatos - ',
        'search_value': search_value
    }

    # renderiza a view
    return render(
        request,
        'contact/index.html',
        context
    )
