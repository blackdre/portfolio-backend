from rest_framework import generics
from .models import Tutorials
from .serializers import TutorialsSerializer


class TutorialsList(generics.ListAPIView):
    queryset = Tutorials.objects.all()
    serializer_class = TutorialsSerializer
