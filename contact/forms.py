from django import forms
from django.core.exceptions import ValidationError
from . import models

class ContactForm(forms.ModelForm): #forms. - tem varios tipos de forms que posso utilizar
    #ModelForm - e um form pageando-se nos models(que se encontram no arq models.py) que ja temos. 
    ...
    class Meta:
        model = models.Contact
        fields = ('first_name','last_name','phone',)

    def clean(self): # class para mostrar os erros:
        
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
