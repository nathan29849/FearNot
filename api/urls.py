from django.urls import path, include
from .views import helloAPI, randomAPI

urlpatterns = [
    path("hello/", helloAPI),
    path("random/<int:id>/", randomAPI),
]

