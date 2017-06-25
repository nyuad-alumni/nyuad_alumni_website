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


class PostNewUser(TestCase):
	"""Test for New User Creation"""
	def setUp(self):
		self.valid_payload = {
		'net_id' : "jj112",
		'first_name' : "Joe",
		'last_name' : "Jean",
		'graduation_year' : "2017",
		'social_networks' : '''
		{"facebook":"https://www.facebook.com/joe.jean3",
		"badjson":"https://www.facebook.com/joe.jean3",
		"linkedin":"https://www.linkedin.com/in/joejean/" }
		'''
		}
		self.invalid_payload = {
		'net_id' : "",
		'first_name' : "Joe",
		'last_name' : "Jean",
		'graduation_year' : "2017",
		'social_networks' : '''
		{"facebook":"https://www.facebook.com/joe.jean3",
		"badjson":"https://www.facebook.com/joe.jean3",
		"linkedin":"https://www.linkedin.com/in/joejean/" }
		'''
		}

	def test_create_a_valid_user(self):
		response = client.post(
			reverse('get_post_users'),
			data=json.dumps(self.valid_payload),
			content_type='application/json'
			)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)



		