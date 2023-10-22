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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    class Meta:
        model = models.Contact
        fields = ('first_name','last_name','phone','email','description','category')
 
    def clean(self):

        cleaned_data = self.cleaned_data
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if first_name == last_name:
            msg = ValidationError(
                'segundo nome não pode ser igual ao primeiro',
                code='invalid'
            )
            
            self.add_error('last_name', msg)

        return super().clean()

        def clean_first_name(self):
            first_name = self.cleaned_data.get('first_name')

            if first_name == 'ABC':
                self.add_error(
                    'first_name',
                    ValidationError(
                        'Veio do add_error', code='invalid'
                )
            )

        return first_name