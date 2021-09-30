from django.urls import path
from .views import Emails

urlpatterns = [
    path('', Emails.as_view()),
]
