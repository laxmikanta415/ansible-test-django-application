from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, response
from .models import Toy
from .serializers import ToySerializer
from rest_framework.decorators import api_view
# Create your views here.

@csrf_exempt
@api_view(['GET', 'POST'])
def toy_list(request):
	if request.method == 'GET':
		toys = Toy.objects.all()
		toys_serializer = ToySerializer(toys, many=True)
		return response.Response(toys_serializer.data)
	if request.method == 'POST':
		toys_serializer = ToySerializer(data = request.data)
		if toys_serializer.is_valid():
			toys_serializer.save()
			return response.Response(toys_serializer.data, status= status.HTTP_201_CREATED)
	return response.Response(toys_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def toy_detail(request, id):
	try:
		toy = Toy.objects.get(pk = id)
	except Toy.DoesNotExist:
		return response.Response(status= status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		toys_serializer = ToySerializer(toy)
		return response.Response(toys_serializer.data)

	if request.method == 'PUT':
		toy_serializer = ToySerializer(toy, data = request.data)
		if toy_serializer.is_valid():
			toy_serializer.save()
			return response.Response(toy_serializer.data)
		return response.Response(toys_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
	if request.method == 'DELETE':
		toy.delete()
		return response.Response(status= status.HTTP_204_NO_CONTENT)




