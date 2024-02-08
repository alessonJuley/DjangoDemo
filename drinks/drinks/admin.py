from django.contrib import admin
from .models import Drink

# register Drink model so it shows up in /admin
admin.site.register(Drink)