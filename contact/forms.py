from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from . import models


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

class RegisterUpdateForm(forms.ModelForm):

    first_name = forms.CharField(
        min_length=2,
        max_length=30,
        required=True,
        help_text='Required.',
        error_messages={
            'min-length':'Plase, add more than 2 letters.'
        }
        )

    last_name = forms.CharField(
            min_length=2,
            max_length=30,
            required=True, # para que seja obrigatorio enviar
            help_text='Required.',
            )
    
    password1 = forms.CharField(
        label = 'Password',
        strip= False,
        widget= forms.PasswordInput(attrs={"autocomplete":"new-password"}),
        help_text= password_validation.password_validators_help_text_html(), #para mostrar o text html para ajudar a preencher os campos
        required=False,
    )

    
    password2 = forms.CharField(
        label = 'Password 2',
        strip= False,
        widget= forms.PasswordInput(attrs={"autocomplete":"new-password"}),
        help_text= 'Use the same password as before.',
        required=False,
    )
    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email', 'username',
        )

    #essa funcao e para poder salvar as senhas na base de dados, sem elas as senhas n seram salvas.
    def save(self, commit=True):

        cleaned_data = self.cleaned_data
        user = super().save(commit=False)

        password = self.cleaned_data.get('password1')

        if password:
            user.set_password(password) # esse metodo 'set_password' e usado para configurar em um usuario, de forma criptografada.and
        
        if commit:
            user.save()

        return user

    #Esse clean e para verificar se as duas senhas sao iguais. 
    def clean(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 or password2: #se a pass 1 ou a 2 for alterada
            if password1 != password2: #verifique se elas sao iguais
                self.add_error('password2', ValidationError('As senhas sao diferentes')) #se n forem iguais,essa sera a mensagem de erro. 

        return super().clean()    

    #Verifica se o email esta a ser alterado ou nao, e se ele n existe ja na lista dos admin
    def clean_email(self):
            email = self.cleaned_data.get('email')
            current_email = self.instance.email
            
            if current_email != email: #quer dizer que  a pessoa quer alterar o email dela, entao...
                if User.objects.filter(emil = email).exists(): # Se existe algum usuario com esse email vai retornar TRUE
                    self.add_error(
                        'email',
                        ValidationError('Ja existe este e-mail', code='invalid')
                    )

            return email
    
    #Verifica se a palavra pass foi alterada e se  existe um erro nela
    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')

        if password1: # se n existe palavra pass nova, entao retornara a a antiga. porq o usuario n mudou de pass 
            
            try:
                password_validation.validate_password(password1)

            except ValidationError as errors: # se tiver erro, vai se pegar esses erros. 

                self.add_error('password1', ValidationError(errors)) #ValidationError(errors) e esse metodo que faz passa os erros para debaixo da caixa

        return password1