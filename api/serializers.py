from rest_framework import serializers
from .models import User, City, Company, Major, \
       PreProfessionalTrack, School, StudyAbroadSite 

class CitySerializer(serializers.ModelSerializer):
	class Meta:
		model = City
		fields = ('city',)

class CompanySerializer(serializers.ModelSerializer):
	class Meta:
		model = Company
		fields = ('name',)
	
class MajorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Major
		fields = ('name',)
	
class PreProfessionalTrackSerializer(serializers.ModelSerializer):
	class Meta:
		model = PreProfessionalTrack
		fields = ('name',)

class SchoolSerializer(serializers.ModelSerializer):
	class Meta:
		model = School
		fields = ('name',)

class StudyAbroadSiteSerializer(serializers.ModelSerializer):
	class Meta:
		model = StudyAbroadSite
		fields = ('name',)
		

class UserSerializer(serializers.ModelSerializer):
	city = CitySerializer()
	school = SchoolSerializer(allow_null=True)
	company = CompanySerializer(allow_null=True)
	majors = MajorSerializer(many=True)
	study_abroad_sites = StudyAbroadSiteSerializer(many=True)
	preprofessional_tracks = PreProfessionalTrackSerializer(allow_null=True,many=True)

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
			'company', 
			'school', 
			'majors',
			'study_abroad_sites',
			'preprofessional_tracks',
			)

	def create(self, validated_data):
		city_name = validated_data.pop('city', None)
		company_name = validated_data.pop('company', None)
		majors = validated_data.pop('majors', None)
		study_abroad_sites = validated_data.pop('study_abroad_sites', None)
		preprofessional_tracks = validated_data.pop('preprofessional_tracks', None)

		if city_name:
			city_name = city_name['city']
			city = City.objects.get(city=city_name)
			validated_data['city'] = city
		if company_name:
			company_name = company_name['name']
			company = Company.objects.get(name=company_name)
			validated_data['company'] = company

		partial_user = User.objects.create(**validated_data)

		user = User.objects.get(pk=partial_user.pk)

		if majors:
			for m in majors:
				major = Major.objects.get(name=m['name'])
				user.majors.add(major)
		if study_abroad_sites:
			for s in study_abroad_sites:
				site = StudyAbroadSite.objects.get(name=s['name'])
				user.study_abroad_sites.add(site)
		if preprofessional_tracks:
			for t in preprofessional_tracks:
				track = PreProfessionalTrack.objects.get(name=t['name'])
				user.preprofessional_tracks.add(track['name'])

		user.save()

		return user

	def update(self, instance, validated_data):
		city = validated_data.get('city', None) 
		company = validated_data.get('company', None)
		school = validated_data.get('school', None)
		majors = validated_data.get('majors', None)
		sa_sites = validated_data.get('study_abroad_sites', None)
		pp_tracks = validated_data.get('preprofessional_tracks', None) 

		instance.net_id = validated_data.get('net_id', instance.net_id)
		instance.first_name = validated_data.get('first_name', instance.first_name)
		instance.last_name = validated_data.get('last_name', instance.last_name)
		instance.graduation_year = validated_data.get('graduation_year', instance.graduation_year)
		instance.preferred_email = validated_data.get('preferred_email', instance.preferred_email)
		instance.social_networks = validated_data.get('social_networks', instance.social_networks)

		if city:
			city = city['city']
			city = City.objects.get(city=city)
			instance.city = city
		if company:
			company = company['name']
			company = Company.objects.get(name=company)
			instance.company = company

		instance.save()

		return instance

