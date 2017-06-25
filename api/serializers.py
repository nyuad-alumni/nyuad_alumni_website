from rest_framework import serializers
from .models import User, City, Company, Major, \
                    PreProfessionalTrack, School, StudyAbroadSite 

class CitySerializer(serializers.ModelSerializer):
	class Meta:
		model = City
		fields = ('country',
				'city',
				'latitude',
				'longitude')

class CompanySerializer(serializers.ModelSerializer):
	class Meta:
		model = Company
		fields = ('name')
		
class MajorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Major
		fields = ('name')
		
class PreProfessionalTrackSerializer(serializers.ModelSerializer):
	class Meta:
		model = PreProfessionalTrack
		fields = ('name')

class SchoolSerializer(serializers.ModelSerializer):
	class Meta:
		model = School
		fields = ('name')


class StudyAbroadSiteSerializer(serializers.ModelSerializer):
	class Meta:
		model = StudyAbroadSite
		fields = ('name')
			

class UserSerializer(serializers.ModelSerializer):
	city = CitySerializer()
	company = CompanySerializer()
	majors = MajorSerializer()
	study_abroads = StudyAbroadSiteSerializer()
	preprofessional_tracks = PreProfessionalTrackSerializer()

	class Meta:
		model = User
		fields = ('net_id',
			'first_name',
			'last_name',
			'graduation_year',
			'preferred_email',
			'social_networks',
			'created_at',
			'updated_at',
			'city',
			'country',
			'company', 
			'majors',
			'study_abroads',
			'preprofessional_tracks',
			)

