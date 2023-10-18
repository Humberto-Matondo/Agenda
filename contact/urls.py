from django.urls import path
from contact import views

app_name= 'contact'

urlpatterns = [
    path('<int:contact_id>/', views.contact, name='contact'), #<int:contact_id> - precisa receber um numero, e o numero sera o contact_id do CONTACT_VIEWS
    path('', views.index, name='index'),
]

