import os
import sys
from datetime import datetime
from pathlib import Path
from random import choice

import django
from django.conf import settings

DJANGO_BASE_DIR = Path(__file__).parent.parent #faz importacao para tras, para que o django pesquise coisas que n estao dentro desse model 
NUMBER_OF_OBJECTS = 1000 # o numero de objeto que seja gerado

sys.path.append(str(DJANGO_BASE_DIR))
os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings'
settings.USE_TZ = False #para ignorar o erro de timezone, para n conf o timezone

django.setup() # Para conf o Django.

if __name__ == '__main__': #Aqui e o inicio do meu SCRIPT
    import faker # Essa e uma biblioteca usada para gerar dados Falsos, usados para testes do app

    from contact.models import Category, Contact

    #Esses dois metodos abaixos deletam todos os contactos criados na BD antes de add os fake, como n queiro que apage COMENTEI-OS
    #Contact.objects.all().delete()
    #Category.objects.all().delete()

    fake = faker.Faker('en-us') #Para que os nomes sejam BR seria: pt_br
    categories = ['Amigo(a)', 'Família','Colega'] #as categorias precisam ja estar criadas no admin Django

    django_categories = [Category(name=name) for name in categories] #list compreehension para gerar as categorias

    for category in django_categories:
        category.save() #salvando as categorias na BD

    django_contacts = [] 

    for _ in range(NUMBER_OF_OBJECTS):
        profile = fake.profile() # Vai tirar do fake um perfil com varias informacoes 
        email = profile['mail'] # Tirou o email dele
        first_name, last_name = profile['name'].split(' ', 1) # Tirou o primeiro e o ultimo nome 
        phone = fake.phone_number() #numero de telefone
        created_date: datetime = fake.date_this_year() #para tirar a data, apenas vai retirar as datas desse ano 
        description = fake.text(max_nb_chars=100) #gera um texto de no maximo 100 palavras que ficara na descricao 
        category = choice(django_categories)  #usando o randon choice, escolhera uma das categorias aleatoriamente 

        #aqui adiciona todos os dados na lista de contactos 
        django_contacts.append(
            Contact(
                first_name=first_name,
                last_name=last_name,
                phone=phone,
                email=email,
                created_date=created_date,
                description=description,
                category=category,
            )
        )

    if len(django_contacts) > 0: # verifica se a lista Django_contacts esta ou n vazia
        Contact.objects.bulk_create(django_contacts) # para criar e salvar na base de dados tudos de uma so vez