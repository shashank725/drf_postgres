from rest_framework import serializers
from .models import assigment

class AssigmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = assigment
        fields = '__all__'