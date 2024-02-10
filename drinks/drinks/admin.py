from django.contrib import admin
from .models import Drink

# created python file
# register Drink model so it shows up in /admin
admin.site.register(Drink)