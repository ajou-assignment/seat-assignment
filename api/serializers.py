from rest_framework import serializers
from .models import UserSet

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSet
        fields = '__all__'