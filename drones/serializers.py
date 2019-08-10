from rest_framework import serializers
from .models import Drone, DroneCategory, Pilot, Competition

class DroneCategorySerializer(serializers.HyperlinkedModelSerializer):
	drones = serializers.HyperlinkedRelatedField(
		many = True,
		read_only = True,
		view_name = 'drone-detail'
		)
	class Meta:
		model = DroneCategory
		fields = ('url','id', 'name','drones',)

class DroneSerializer(serializers.HyperlinkedModelSerializer):
	drone_category = serializers.SlugRelatedField(queryset = DroneCategory.objects.all(), slug_field='name')
	class Meta:
		model = Drone		
		fields = ('url', 'id', 'drone_category','name','manufacturing_date','has_it_competed','created',)

class CompetitionSerializer(serializers.HyperlinkedModelSerializer):
	
	class Meta:
		model = Competition
		fields = ('id','pilot','drone','distance_in_feet','distance_achievement_date',)

class PilotSerializer(serializers.HyperlinkedModelSerializer):
	competitions = CompetitionSerializer(many=True, read_only=True)
	gender =  serializers.ChoiceField(choices = Pilot.GENDER_CHOICES)
	gender_description = serializers.CharField(source = 'get_gender_display', read_only=True)
	class Meta:
		model = Pilot
		fields = ('id','name','gender','gender_description','races_count','created','competitions',)

class PilotCompetitionSerializer(serializers.ModelSerializer):
	drone = serializers.SlugRelatedField(queryset= Drone.objects.all(), slug_field='name')
	pilot = serializers.SlugRelatedField(queryset= Pilot.objects.all(), slug_field= 'name')

	class Meta:
		model = Competition
		fields = ('url','pk','distance_in_feet','distance_achievement_date','drone', 'pilot', )