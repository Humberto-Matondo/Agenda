from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from contact.forms import ContactForm
from contact.models import Contact


@login_required(login_url='contact:login') #Para caso n esteja logado, redirecionar isso para contact:login
def create(request):
    form_action = reverse('contact:create')
    if request.method == 'POST':

        form = ContactForm(request.POST, request.FILES)

        context = {
            'form': form,
            'form_action': form_action,
        }

        if form.is_valid(): 
            contact = form.save(commit=False) 
            contact.owner = request.user # para atribuir um proprietario ao contact criado
            contact.save()
            messages.success(request, 'Contact Created') #Vai informar que o ficheiro foi salvado
            return redirect('contact:contact', contact_id = contact.pk) 
        
        return render(
            request,
            'contact\create.html',
            context,
        )

    context = {
        'form': ContactForm(),
        'form_action': form_action,
        }
    
    return render(
        request,
        'contact\create.html',
        context,
    )

@login_required(login_url='contact:login')
def update(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id, show = True, owner = request.user) #para que n de para mudificarem o contact em outro usuario.

    form_action = reverse('contact:update', args=(contact_id,))

    if request.method == 'POST':

        form = ContactForm(request.POST,request.FILES,instance=contact)

        context = {
            'form': form,
            'form_action': form_action,
        }

        if form.is_valid(): 
            contact = form.save() 
            messages.success(request, 'Contact Updated') #Vai informar que o ficheiro foi salvado
            return redirect('contact:update', contact_id = contact.pk) 
        
        return render(
            request,
            'contact\create.html',
            context,
        )

    context = {
        'form': ContactForm(instance=contact),
        'form_action': form_action,
        }
    
    return render(
        request,
        'contact\create.html',
        context,
    )

@login_required(login_url='contact:login') 
def delete(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id, show = True, owner = request.user)

    confirmation = request.POST.get('confirmation', 'no')

    if confirmation == 'yes':
        contact.delete()
        messages.success(request, 'Contact Deteted') #Vai informar que o ficheiro foi salvado
        return redirect('contact:index')

    return render(
        request, 
        'contact/contact.html',
        {
            'contact': contact,
            'confirmation':confirmation,
        }

    )
