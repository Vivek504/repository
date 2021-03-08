from django.urls import path
from . import views

urlpatterns = [
    path("home",views.home,name="home"),
    path("onewayTrip",views.onewayTrip,name="onewayTrip"),
    path("roundTrip",views.roundTrip,name="roundTrip")
]