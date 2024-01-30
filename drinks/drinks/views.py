from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status 
# file to create all endpoints

@api_view (['GET', 'POST'])
def drink_list(request):

          if request.method == 'GET':
                  # get all the drinks
                  drinks = Drink.objects.all()
                  # serialize drinks
                  serializer = DrinkSerializer(drinks, many=True)
                  # return as json
                  #           if you want to return it as list:
                  #                     return JsonResponse(serializer.data, safe=False)
                  #           if you want to return as object: list
                  return JsonResponse({'drinks': serializer.data})
          if request.method == 'POST':
                  # get all the drinks from request
                  serializer = DrinkSerializer(data=request.data)
                  # check if data is valid
                  if serializer.is_valid():
                          # save data you took
                          serializer.save()
                          return Response(serializer.data, status=status.HTTP_201_CREATED)
                  # deserialize drink
                  
                  # create a drink