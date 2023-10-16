from django.db import models
from django.utils import timezone

# Create your models here.

# id(primary key - criado automatico pelo django)

# first_name(string), last_name(string), phone(string)
# email(string), created_date(date), description(test)

# category(foreign key), show(boolean), picture (imagem)

# owner(foreign key)
class Contact(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank=True)
    created_date = models.DateField(default=timezone.now)
    description = models.TextField(blank=True)

    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to= 'picture/%Y/%m/') #dentro da pastas media, vai criar pasta picture, 
                                # dentro dela vai criar pasta do ano*(%Y) atuas, dentro dela vai criar pasta do mes(%m) atuas
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    