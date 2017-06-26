import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import User, City, Company, Major,\
					 PreProfessionalTrack, School, StudyAbroadSite
from ..serializers import CitySerializer, CompanySerializer, MajorSerializer,\
						UserSerializer

# Initialize the APIClient App
client = Client()

class GetAllCompaniesTest(TestCase):
	""" Test module for GET all companies API """
	def SetUp(self):
		Company.objects.create(name="Namshi")

	def test_get_all_companies_associated_with_user(self):
		# Get API Response
		response = client.get(reverse('get_companies'))
		# Get data from db
		companies = Company.objects.filter(users__isnull=False)
		serializer = CompanySerializer(companies, many=True)
		self.assertEqual(response.data, serializer.data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)


class UserSerializerTest(TestCase):
	"""Test for New User Creation"""
	@classmethod
	def setUpTestData(cls):
		cls.city = City.objects.create(city="Abu Dhabi")
		cls.major = Major.objects.create(name="Computer Science")
		cls.site = StudyAbroadSite.objects.create(name="Florence")
		cls.user = User.objects.create(
			net_id = "jj1110",
			first_name = "Jonas",
			last_name = "Jean",
			graduation_year = "2017",
			social_networks = '''
			{"facebook":"https://www.facebook.com/joe.jean3",
			"linkedin":"https://www.linkedin.com/in/joejean/" }
			''',
			preferred_email = 'jonas.jean@namshi.com'
		)
		cls.user.city = cls.city
		cls.user.majors.add(cls.major)
		cls.user.study_abroad_sites.add(cls.site)
		cls.user.save()

	def setUp(self):		
		self.valid_create_payload = {
		'net_id' : "jj112",
		'first_name' : "Joe",
		'last_name' : "Jean",
		'graduation_year' : "2017",
		'social_networks' : '''
		{"facebook":"https://www.facebook.com/joe.jean3",
		"linkedin":"https://www.linkedin.com/in/joejean/" }
		''',
		'preferred_email': 'joe.jean@namshi.com',
		'city' : {"city":"Abu Dhabi"},
		'majors': [{"name":"Computer Science"}],
		'study_abroad_sites': [{"name":"Florence"}]
		}

		self.valid_update_payload = {
		'social_networks' : '''
		{"facebook":"https://www.facebook.com/joe.jean3",
		"linkedin":"https://www.linkedin.com/in/joejean/" }
		''',
		'preferred_email': 'joe.jean@namshi.com',
		'city' : {"city":"Abu Dhabi"},
		'majors': [{"name":"Computer Science"}]
		}

		self.invalid_create_payload = {
		'net_id' : "",
		'first_name' : "Joe",
		'last_name' : "Jean",
		'graduation_year' : "2017",
		'social_networks' : '''
		{"facebook":"https://www.facebook.com/joe.jean3",
		"linkedin":"https://www.linkedin.com/in/joejean/" }
		'''
		}

	def test_create_user_with_a_valid_payload(self):
		response = client.post(
			reverse('get_post_users'),
			data=json.dumps(self.valid_create_payload),
			content_type='application/json'
			)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

	def test_create_user_with_an_invalid_payload(self):
		response = client.post(
			reverse('get_post_users'),
			data=json.dumps(self.invalid_create_payload),
			content_type='application/json'
			)
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

	def test_update_nonexistent_user(self):
		response = client.put(
			reverse('get_delete_update_user', args=['NOEXIST123']),
			data=json.dumps(self.valid_update_payload),
			content_type='application/json'
			)
		self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

	def test_update_user_with_valid_payload(self):
		response = client.put(
			reverse('get_delete_update_user', args=['jj1110']),
			data=json.dumps(self.valid_update_payload),
			content_type='application/json'
			)
		
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_get_existing_user(self):
		response = client.get(
			reverse('get_delete_update_user', args=['jj1110']),
			content_type='application/json'
			)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.data['net_id'], 'jj1110')
		self.assertEqual(len(response.data['study_abroad_sites']), 1)
		self.assertEqual(response.data['study_abroad_sites'][0]['name'],'Florence')

	