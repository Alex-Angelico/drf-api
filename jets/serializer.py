from rest_framework import serializers
from .models import Jets

class JetSerializer(serializers.ModelSerializer):
		class Meta:
				fields = ('id', 'name', 'country_origin', 'description', 'engine_count', 'added_by', 'added')
				model = Jets