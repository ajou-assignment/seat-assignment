from rest_framework import serializers
from .models import *

class mySerializer(serializers.ModelSerializer):
    class Meta:
        model = Hist_Match
        fields = '__all__'