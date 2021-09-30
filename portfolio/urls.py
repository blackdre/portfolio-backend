from django.urls import path
from .views import TutorialsList

urlpatterns = [
    path('', TutorialsList.as_view()),
]
