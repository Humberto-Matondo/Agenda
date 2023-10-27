from django.contrib import auth, messages
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render

from contact.forms import RegisterForm, RegisterUpdateForm


def register(request):

    form = RegisterForm()


    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'User Registed') 
            return redirect('contact:login') #vai mudar de pagina, e aparecer a mgs por la.

    return render(
        request,
        'contact/register.html', 
        {
            'form': form
        }
    )

def login_view(request):
    
    form = AuthenticationForm(request)
    
    if request.method == 'POST': 
        form = AuthenticationForm(request, data= request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user) #Para autenticar o usuario e permitir que ele entre
            messages.success(request, 'Login Successfully') 
            return redirect('contact:index')
        
    return render(
        request,
        'contact/login.html', 
        {
            'form': form
        }
    )

def logout_view(request):
    auth.logout(request)
    return redirect('contact:login')

def user_update(request):

    form = RegisterUpdateForm(instance=request.user)

    if request.method != 'POST':

        return render(
            request,
            'contact/user_update.html', 
            {
            'form': form
            }
        )
    
    form = RegisterUpdateForm(data=request.POST, instance=request.user)

    if not form.is_valid():
        
        return render(
            request,
            'contact/user_update.html', 
            {
            'form': form
            }
        )

    form.save()
    messages.success(request, 'Updated Successfully') 
    return redirect('contact:index')