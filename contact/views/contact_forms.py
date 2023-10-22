from django.shortcuts import render, redirect
from contact.forms import ContactForm

def create(request):

    if request.method == 'POST':

        form = ContactForm(request.POST)
        context = {
            'form': form,
        }

        if form.is_valid(): # Se passar daqui significa que n tem nenhum ERRO no meu formulario entao ENVIA os dados na BD
            form.save() # SALVA O FORMULARIO COM OS DADOS DO CONTACTO NA BD
            return redirect('contact:create') # apois salvar os dados vai redirecionar a pagina para a mesma pagina(ficara como se a pagina actualizou-se)
                            #usaremos isso para limpar o formulario, para que o usuario n criei dois contactos identicos.

        return render(
            request,
            'contact\create.html',
            context,
        )

    context = {
        'form':ContactForm()
    }
    
    return render(
        request,
        'contact\create.html',
        context,
    )