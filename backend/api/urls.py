from django.urls import path, include
from .views import helloAPI, randomAPI, getCoronaAPI

urlpatterns = [
    path("hello/", helloAPI),
    path("random/<int:id>/", randomAPI),
    path('corona/<str:start>/<str:end>/', getCoronaAPI),
]

