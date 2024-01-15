# from django.shortcuts import render, redirect
from contact.models import Contact
from django.shortcuts import render, redirect, get_object_or_404
from contact.forms import ContactForm
from contact.models import Contact

# muda dinamicamente uma url
from django.urls import reverse

# https://docs.djangoproject.com/en/4.2/topics/pagination/
from django.core.paginator import Paginator

# Create your views here.

def create(request):

    form_action = reverse('contact:create')
    

    # se o formulario é enviado 
    # formulario enviado
    if request.method == 'POST':

        form = ContactForm(request.POST, request.FILES)
        context = {
            'form': form,
            'form_action': form_action,
            'titulo_view': 'Criar novo contato'
        }

        if form.is_valid():
            # contact = form.save(commit=False)
            # contact.show = False
            # contact.save()
            contact = form.save()

            return redirect('contact:update', contact_id=contact.pk)

        return render(
            request,
            'contact/create.html',
            context
        )
    # fim do envio do formulario
  
    # leva para a view o ContactForm com os inputs
    context = {
        'form': ContactForm(),
        'form_action': form_action,
        'titulo_view': 'Criar novo contato'
    }

    return render(
        request,
        'contact/create.html',
        context
    )



def update(request, contact_id):

    contact = get_object_or_404(
        Contact, pk=contact_id, show=True
    )

    form_action = reverse('contact:update', args=(contact_id,))

    # se o formulario é enviado 
    # formulario enviado
    if request.method == 'POST':

        form = ContactForm(request.POST, request.FILES, instance=contact)
        context = {
            'form': form,
            'form_action': form_action,
            'titulo_view': 'Atualizar contato'
        }

        if form.is_valid():
            # contact = form.save(commit=False)
            # contact.show = False
            # contact.save()
            contact = form.save()

            return redirect('contact:update', contact_id=contact.pk)

        return render(
            request,
            'contact/create.html',
            context
        )
    # fim do envio do formulario
  
    # leva para a view o ContactForm com os inputs
    context = {
        'form': ContactForm(instance=contact),
        'form_action': form_action,
        'titulo_view': 'Atualizar contato'
    }

    return render(
        request,
        'contact/create.html',
        context
    )


def delete(request, contact_id):
    contact = get_object_or_404(
        Contact, pk=contact_id, show=True
    )

    confirmation = request.POST.get('confirmation', 'no')

    if confirmation == 'yes':
        contact.delete()
        return redirect('contact:index')


    #contact.delete()
    #return redirect('contact:index')

    return render(
        request,
        'contact/contact.html',
        {
            'contact': contact,
            'confirmation': confirmation
        }
    )