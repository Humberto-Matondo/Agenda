from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from contact.models import Contact

# Create your views here.
def index(request):

    contacts = Contact.objects.filter(show=True).order_by('-id') 
    context = {
        'contacts': contacts, 
        'site_title': 'Contactos - '
    }

    return render(
        request,
        'contact\index.html',
        context,
    )

def contact(request, contact_id):

    single_contact = get_object_or_404(Contact.objects.filter(id=contact_id,show=True)) # O get...404 pode-se manipular tmbm dessa forma: (Contact, pk=contact_id),  

    site_title = f'{single_contact.first_name} {single_contact.last_name} - '

    context = {
        'contact': single_contact, 
        'site_title': site_title,
    }

    return render(
        request,
        'contact\contact.html',
        context,
    )

def search(request):

    search_value = request.GET.get('h','').strip() # Para se pegar o valor do dicionario de request...
                                        # get('h','') - caso o valor do 'h' for encontrado retorna o Valor, 
                                        # Caso n Encontrar vai retornar uma string VAZIA. 
                                        # O .strip() serve para remover os espacos do comeco e do final, escrito pelo usuario

    #Caso o usuario digitar apenas espacoes, sem nenhum valor:
    if search_value == '':
        return redirect('contact:index') # Vai redirecionar-lo para a pagina inicial, como se nada tivesse acontecido. 

    contacts = Contact.objects.\
        filter(show=True).\
        filter( 
            Q(first_name__icontains= search_value) | 
            Q(last_name__icontains= search_value) |
            Q(phone__icontains= search_value) |
            Q(email__icontains= search_value)
            ).\
        order_by('-id') 
        # para usar os filters look up, primeiro tens que add o campo que procuras 
        # e depois dois Underlines(__) e o filter.
        # o Q()- e uma funcao que me permite usar o "|" = OR, pq a virgula(,) funciona como AND
        # Q1() | Q1() = se o nome estiver no Q1 ou Q2 mostra ele... ou o numero de tel, ou o email
        #para que de para buscarmos pelo nome completo, teriamos que ter um valor FULLNAME e comparariamos ele com o search_value

    context = {
        'contacts': contacts, 
        'site_title': 'Search - '
    }

    return render(
        request,
        'contact\index.html',
        context,
    )
