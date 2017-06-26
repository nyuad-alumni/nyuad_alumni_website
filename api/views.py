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
	except Exception:
		try:
			user = User.objects.get(net_id=id)

		except User.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = UserSerializer(user)
		return Response(serializer.data)

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
	if request.method == 'POST':
		data = {
			'net_id' : request.data.get('net_id'),
			'first_name' : request.data.get('first_name'),
			'last_name' : request.data.get('last_name'),
			'graduation_year' : request.data.get('graduation_year'),
			'social_networks' : request.data.get('social_networks'),
			'preferred_email' : request.data.get('preferred_email'),
			'city' : request.data.get('city'), 
			'company' : request.data.get('company'),  
			'school' : request.data.get('school'),  
			'majors' : request.data.get('majors'), 
			'study_abroad_sites' : request.data.get('study_abroad_sites'), 
			'preprofessional_tracks' : request.data.get('preprofessional_tracks'), 
		}

		serializer = UserSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)

		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
			

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




