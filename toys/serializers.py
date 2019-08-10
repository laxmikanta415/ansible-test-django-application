from rest_framework import serializers
from toys.models import Toy

class ToySerializer(serializers.ModelSerializer):
	class Meta:
		model = Toy
		fields = ('pk', 'name', 'description', 'toy_category', 'release_date', 'was_included_in_home',)