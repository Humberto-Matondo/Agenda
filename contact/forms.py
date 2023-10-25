from . import models
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
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
    first_name = forms.CharField(
        required= True,
        min_length= 3,
    )
    
    last_name = forms.CharField(
        required= True,
        min_length= 3,
    )

    email = forms.EmailField()
    # esses campos acima(first_name, last_name, e email) servem para forcar o usuarui a informar os dados
    # sem isso acima os usuarios podem n digitar aquelas informacoes
    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email', 'username', 'password1',
            'password2',
        )

        def clean_email(self):
            email = self.cleaned_data.get('email')
            
            if User.objects.filter(emil = email).exists(): # Se existe algum usuario com esse email vai retornar TRUE
                self.add_error(
                    'email',
                    ValidationError('Ja existe este e-mail', code='invalid')
                )

            return email
