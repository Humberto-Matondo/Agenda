from . import models
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm

class ContactForm(forms.ModelForm): 
    picture = forms.ImageField(
        widget= forms.FileInput(
            attrs={
                'accept':'image/*', # Essa linha diz para ceitar qualquer imagem, posso restringir se quiser.
            }
        )
    )
    class Meta:
        model = models.Contact
        fields = (
            'first_name','last_name','phone','email','description',
            'category','picture'
            )
 
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

class RegisterForm(UserCreationForm):
    ...