from django.urls import path
from .views import CMSList

urlpatterns = [
    path('', CMSList.as_view()),
]
