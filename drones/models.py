from django.db import models

# Create your models here.
class DroneCategory(models.Model):
	name = models.CharField(max_length=100, unique=True)

	class Meta:
		ordering = ('name',)

	def __str__(self):
		return self.name

class Drone(models.Model):
	drone_category = models.ForeignKey(DroneCategory, related_name = 'drones', on_delete = models.CASCADE)
	name = models.CharField(max_length=100, unique=True)
	manufacturing_date = models.DateTimeField()
	has_it_competed = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add = True)

	class Meta:
		ordering = ('name',)

	def __str__(self):
		return self.name

class Pilot(models.Model):
	GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'))
	name = models.CharField(max_length=100, unique=True)
	gender = models.CharField(choices = GENDER_CHOICES, default='M', max_length=2)
	races_count = models.IntegerField()
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ('name',)

	def __str__(self):
		return self.name

class Competition(models.Model):
	pilot = models.ForeignKey(Pilot, related_name='pilots', on_delete=models.CASCADE)
	drone = models.ForeignKey(Drone, related_name='drones', on_delete=models.CASCADE)
	distance_in_feet = models.DecimalField(max_digits=20, decimal_places=4)
	distance_achievement_date = models.DateTimeField()

	class Meta:
		# Order by distance in descending order
		ordering = ('-distance_in_feet',)

