from django.urls import path
from . import views

urlpatterns = [
    path("view_payment_history",views.view_payment_history,name="view_payment_history"),
    path("view_ticket",views.view_ticket,name="view_ticket"),
    path("payment_method",views.payment_method,name="payment_method"),
    path("make_payment",views.make_payment,name="make_payment"),
    path("flight<int:flight_id><int:travellers><str:cls>",views.payment,name="flight")
]