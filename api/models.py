from django.db import models
import json

class City(models.Model):
	country = models.CharField(max_length=60)
	city = models.CharField(max_length=60)
	region = models.CharField(max_length=60)
	latitude = models.CharField(max_length=60)
	longitude = models.CharField(max_length=60) 

	def __str__(self):     
		return "City %s " % self.city

class Company(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return "Company %s" % self.name
		 
class School(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return "School %s" % self.name

class Major(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return "Major %s" % self.name

class PreProfessionalTrack(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return "Pre-professional Track %s" % self.name

class StudyAbroadSite(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return "Study Abroad Site %s" % self.name


class User(models.Model):
	net_id = models.CharField(max_length=12)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	graduation_year = models.CharField(max_length=4)
	preferred_email = models.CharField(max_length=40) 
	social_networks = models.CharField(max_length=400, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	city = models.ForeignKey(
		City, 
		on_delete=models.SET_NULL,
		null=True,
		related_name='users'
	)
	company = models.ForeignKey(
		Company,
		on_delete=models.SET_NULL,
		null=True,
		related_name='users'
	)
	school = models.ForeignKey(
		School,
		on_delete=models.SET_NULL,
		null=True,
		related_name='users'
	)
	majors = models.ManyToManyField(Major)
	study_abroads = models.ManyToManyField(StudyAbroadSite)
	preprofessional_tracks = models.ManyToManyField(PreProfessionalTrack)

	def get_social_networks_links(self):
		try:
			return json.loads(self.social_networks)
		except Exception as e:
			return {}

	def __str__(self):
		return "User %s %s. Netid %s" % (self.first_name, self.last_name, self.net_id)
 



	
