from rest_framework import generics
from .models import Contact
from .serializers import ContactSerializer
from django.contrib import messages
from django.core.mail import send_mail


class Contact(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
