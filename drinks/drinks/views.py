from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer

# file to create all endpoints
def drink_list(request):
          # get all the drinks
          drinks = Drink.objects.all()
          # serialize drinks
          serializer = DrinkSerializer(drinks, many=True)
          # return json list return JsonResponse(serializer.data, safe=False)
          # return json object:list return JsonResponse({'drinks': serializer.data}, safe=False)
          return JsonResponse({'drinks': serializer.data}, safe=False)