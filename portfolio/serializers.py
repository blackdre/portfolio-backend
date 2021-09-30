from rest_framework import serializers
from .models import Tutorials


class TutorialsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Tutorials
