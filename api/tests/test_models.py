from django.test import TestCase
from ..models import User, City, Company, School, Major,\
					PreProfessionalTrack, StudyAbroadSite

class CompanyTest(TestCase):
	def setUp(self):
		Company.objects.create(name='Namshi')
		Company.objects.create(name='ARM')

	def test_string_representation(self):
		namshi = Company.objects.get(name="Namshi")
		self.assertEqual(str(namshi), "Company Namshi")

class UserTest(TestCase):
	def setUp(self):
		User.objects.create(
			net_id = "jj1347",
			first_name = "Joe",
			last_name = "Jean",
			graduation_year = "2017",
			social_networks = '''
			{"facebook":"https://www.facebook.com/joe.jean3",
			"linkedin":"https://www.linkedin.com/in/joejean/" }
			'''
		)

		User.objects.create(
			net_id = "jj112",
			first_name = "Joe",
			last_name = "Jean",
			graduation_year = "2017",
			social_networks = '''
			{"facebook":"https://www.facebook.com/joe.jean3",
			badjson:"https://www.facebook.com/joe.jean3",
			"linkedin":"https://www.linkedin.com/in/joejean/" }
			'''
		)

	def test_get_social_networks_links(self):
		user = User.objects.get(net_id="jj1347")
		facebook_link = user.get_social_networks_links()['facebook']
		linkedin_link = user.get_social_networks_links()['linkedin']
		self.assertEqual("https://www.facebook.com/joe.jean3", facebook_link)
		self.assertEqual("https://www.linkedin.com/in/joejean/", linkedin_link)
	
	def test_empty_social_networks_dict(self):
		user = User.objects.get(net_id="jj112")
		self.assertEqual({}, user.get_social_networks_links())