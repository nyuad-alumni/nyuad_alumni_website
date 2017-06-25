from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import User, City, Company, Major, \
                    PreProfessionalTrack, School, StudyAbroadSite 
from .serializers import CitySerializer, CompanySerializer, MajorSerializer,\
						UserSerializer


@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_user(request, id):
	try:
		user = User.objects.get(pk=id)
	except User.DoesNotExist:
		try:
			user = User.objects.get(net_id=id)
		except User.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		return Response({})

	elif request.method == 'DELETE':
		return Response({})

	elif request.method == 'PUT':
		return Response({})

@api_view(['GET', 'POST'])
def get_post_users(request):
	if request.method == 'GET':
		users = User.objects.all()
		serializer = UserSerializer(users, many=True)
		
		return Response(serializer.data)
	else:
		return Response({})

@api_view(['GET'])
def get_cities(request):
	cities = City.objects.filter(users__isnull=False)
	serializer = CitySerializer(cities, many=True)
	
	return Response(serializer.data)

@api_view(['GET'])
def get_companies(request):
	companies = Company.objects.filter(users__isnull=False)
	serializer = CompanySerializer(companies, many=True)

	return Response(serializer.data)




