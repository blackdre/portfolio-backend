from rest_framework import serializers
from .models import Emails


class Emailserializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Emails
