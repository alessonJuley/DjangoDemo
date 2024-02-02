from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer

# endpoints (certain URL that you can access data from)
# add URL of drink_list in urls.py file after making functions
def drink_list(request):
          # get all the drinks by accessing Drink Class
          # serialize python object to json using DrinkSerializer
          # return json object:list

          drinksListObject = Drink.objects.all()
          serializer = DrinkSerializer(drinksListObject, many=True)
          return JsonResponse({'drinks': serializer.data}, safe=False)

