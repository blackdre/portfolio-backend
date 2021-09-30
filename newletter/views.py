from rest_framework import generics
from .models import Emails
from .serializers import Emailserializer


class Emails(generics.ListCreateAPIView):
    queryset = Emails.objects.all()
    serializer_class = Emailserializer
