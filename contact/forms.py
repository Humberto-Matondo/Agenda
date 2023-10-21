from django import forms
from django.core.exceptions import ValidationError
from . import models

class ContactForm(forms.ModelForm): 
    #codigo do widget: 
    first_name = forms.CharField(
        widget = forms.TextInput(
            attrs={
                'placeholder':'digite seu primeiro nome',
            }
        ),
        label= 'Primeiro nome',
        help_text = 'testo de ajuda para o usuario',
    )

    class Meta:
        model = models.Contact
        fields = ('first_name','last_name','phone',)

    def clean(self): 
        
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
