from django.shortcuts import render, redirect
from contact.forms import RegisterForm
from django.contrib import messages

def register(request):

    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'User Registed') #Vai informar que o ficheiro foi salvado
            return redirect('contact:index') #vai mudar de pagina, e aparecer a mgs por la.

    return render(
        request,
        'contact/register.html', 
        {
            'form': form
        }
    )