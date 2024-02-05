from django.db import models

class Drink(models.Model):
        name = models.CharField(max_length=200)
        description = models.CharField(max_length=500)

        def __str__(self):
                return self.name + ' ' + self.description
          
class Bread(model.Models):
        name = models.CharField(max_length=200)
        category = models.CharField(max_length=300)
        description = models.CharField(max_length=500)
        price = models.DecimalField(max_digits=5, decimal_places=2)
        stock = models.PositiveIntegerField()