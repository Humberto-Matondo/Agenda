from django.contrib import admin
from contact import models


# Register your models here.
@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    
    list_display = 'id', 'first_name', 'last_name', 'email', 'phone', 'show', 
    ordering = '-id', 
    search_fields = 'id', 'first_name', 'last_name',
    list_per_page = 10 
    list_max_show_all = 100 
    list_display_links = 'first_name', 'last_name', 'email', 'phone',
    list_editable = 'show', #para poder editar os show de forma rapida 

    
@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = 'name',
    ordering = 'id',