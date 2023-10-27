from django.urls import path

from contact import views

app_name= 'contact'

urlpatterns = [
    path('search/', views.search, name='search'),  
    path('', views.index, name='index'),
    
    #contact(CRUD)
    path('contact/<int:contact_id>/', views.contact, name='contact'), 
    path('contact/create/', views.create, name='create'), 

    path('contact/<int:contact_id>/update/', views.update, name='update'), 
    path('contact/<int:contact_id>/delete/', views.delete, name='delete'), 
    
    #user
    path('user/create/', views.register, name='register'), 
    path('user/login/', views.login_view, name='login'), 
    path('user/logout/', views.logout_view, name='logout'), 
    path('user/update/', views.user_update, name='user_update'),  
]