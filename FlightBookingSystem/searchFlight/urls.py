from django.urls import path
from . import views

urlpatterns = [
    path("home",views.home,name="home"),
    path("flight_details",views.flight_details,name="flight_details")
]