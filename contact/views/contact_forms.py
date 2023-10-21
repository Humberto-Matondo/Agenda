from django.shortcuts import render
from contact.forms import ContactForm

def create(request):

    #FORMULARIO COM POST: 
    if request.method == 'POST':
        context = {
            'form':ContactForm(request.POST)
        }

        return render(
            request,
            'contact\create.html',
            context,
        )

    #FORMULARIO LIMPO:
    context = {
        'form':ContactForm()
    }
    
    return render(
        request,
        'contact\create.html',
        context,
    )