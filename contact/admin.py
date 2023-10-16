from django.contrib import admin
from contact import models


# Register your models here.
@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    
    #list_display- mostra as tabelas listadas
    list_display = 'id', 'first_name', 'last_name', 'email', 'phone',
    
    #ordering- faz a ordenacao, pode ser pelo nome, data, id e etc
    ordering = 'id', #Vai ordenar apartir dos Ids(-id para decrecer)
    
    #list_filter - Cria filtracoes, podes filtrar por data, categoria, etc 
    #list_filter =  'created_date',
    
    #search_filter - Barra de besquisa, aqui dizes o que queres pesquisa 
    search_fields = 'id', 'first_name', 'last_name',
    list_per_page = 10 # Para mostrar X contactos de cada vez.
    list_max_show_all = 100 # Para limitar a quantidade de contact a 
                            # ver de uma so vez no "MOSTRAR TUDO"

    #Faz a edicao dos selecionados sem precisar entrar no contact.
    #list_editable = 'first_name', 'last_name', #N acho util.

    #Gerar link, para entrares no perfil automaticamente
    list_display_links = 'first_name', 'last_name', 'email', 'phone',

     