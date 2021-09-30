from rest_framework import serializers
from .models import CMS


class CMSSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = CMS
