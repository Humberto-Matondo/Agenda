from django.db import models
from django.utils import timezone

# Create your models here.

# id(primary key - criado automatico pelo django)

# first_name(string), last_name(string), phone(string)
# email(string), created_date(date), description(test)

# category(foreign key), show(boolean), owner(foreign key)
# picture (imagem)
class Contact(models.Model):

    first_name = models.CharField(max_length=50)

    last_name = models.CharField(max_length=50, blank=True)

    phone = models.CharField(max_length=50)

    email = models.EmailField(max_length=254, blank=True)

    created_date = models.DateField(default=timezone.now)

    description = models.TextField(blank=True)