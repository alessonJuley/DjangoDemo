from rest_framework import serializers
from .models import Drink

# describe the process of going from a python object to json
class DrinkSerializer(serializers.ModelSerializer):
          # Metadata that will describe the model
          class Meta: 
                  model = Drink
                  fields = ['id', 'name', 'description']