from rest_framework import generics
from .models import Projects
from .serializers import ProjectsSerializer


class ProjectsList(generics.ListAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer
