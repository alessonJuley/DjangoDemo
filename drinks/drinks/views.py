from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# endpoints (certain URL that you can access data from)
# add URL of drink_list in urls.py file after making functions

# function drink_list Reads all the data
@api_view(['GET','POST'])
def drink_list(request):
          if request.method == 'GET':
                    # get all the drinks (data) by accessing Drink class
                    # serialize python object to json using DrinkSerializer
                    # return json object:list

                    drinksListObject = Drink.objects.all()
                    serializer = DrinkSerializer(drinksListObject, many=True)
                    return JsonResponse({'drinks': serializer.data}, safe=False)
          if request.method == 'POST':
                    # get json object:list
                    # deserialize json to python object
                    # make sure to check the json data you got
                    # save new python object (new drink)
                    serializer = DrinkSerializer(data=request.data)
                    if serializer.is_valid():
                              serializer.save()
                              return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def drink_detail(request, id):
          try:
                    drinkObjectID = Drink.objects.get(pk=id)
          except Drink.DoesNotExist:
                    return Response(status=status.HTTP_404_NOT_FOUND)
          
          if request.method == 'GET':
                    serializer = DrinkSerializer(drinkObjectID)
                    return Response(serializer.data)
          elif request.method == 'PUT':
                    serializer = DrinkSerializer(drinkObjectID, data=request.data)
                    if serializer.is_valid():
                              serializer.save()
                              return Response(serializer.data)
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
          elif request.method == 'DELETE':
                    pass