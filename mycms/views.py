from rest_framework import generics
from .models import CMS
from .serializers import CMSSerializer


class CMSList(generics.ListAPIView):
    queryset = CMS.objects.all()
    serializer_class = CMSSerializer
