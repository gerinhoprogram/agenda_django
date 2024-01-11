from django.shortcuts import render, redirect
from contact.models import Contact
from django.shortcuts import get_object_or_404, render

# Create your views here.

def index(request):
    contacts = Contact.objects.all().filter(show=True).order_by('-id')[0:10]

    # mostra a query
    # print(contacts.query)

    context = {
        'contacts': contacts,
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

    contacts = Contact.objects.all().filter(show=True).order_by('-id')[0:10]

    # mostra a query
    # print(contacts.query)

    context = {
        'contacts': contacts,
        'site_title': 'Contatos - '
    }

    return render(
        request,
        'contact/index.html',
        context
    )
