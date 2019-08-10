from django.db import models

# Create your models here.

class Toy(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=80, default='')
	description = models.TextField(blank=True, default='')
	toy_category = models.CharField(max_length=200)
	release_date = models.DateTimeField()
	was_included_in_home = models.BooleanField(default=False)

	class Meta:
		ordering = ('name',)




