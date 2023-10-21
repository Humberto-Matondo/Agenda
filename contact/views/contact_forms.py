from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from contact.models import Contact
from django.core.paginator import Paginator

from django import forms
from django.core.exceptions import ValidationError
class ContactForm(forms.ModelForm): #forms. - tem varios tipos de forms que posso utilizar
    #ModelForm - e um form pageando-se nos models(que se encontram no arq models.py) que ja temos. 
    ...
    class Meta:
        model = Contact
        fields = ('first_name','last_name','phone',)

    def clean(self): # class para mostrar os erros:
        cleaned_data = self.cleaned_data

        self.add_error(
            'first_name',
            ValidationError(
                'Mensagem de erro',
                code='invalid'
            )
        )
        self.add_error(
            'first_name',
            ValidationError(
                'Mensagem de erro 2',
                code='invalid'
            )
        )
        
        return super().clean()

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