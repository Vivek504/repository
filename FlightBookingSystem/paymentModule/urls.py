from django.urls import path
from . import views

urlpatterns = [
    path("view_payment_history",views.view_payment_history,name="view_payment_history"),
    path("payment_method",views.payment_method,name="payment_method"),
    path("make_payment",views.make_payment,name="make_payment"),
    path("flight<int:flight_id>,<int:travellers>,<str:cls>",views.payment,name="flight"),
    path("roundtrip_flight<int:flight_id1>,<int:flight_id2>,<int:travellers>,<str:cls>",views.roundtrip_payment,name="roundtrip_flight"),
    path("roundtrip_payment_method",views.roundtrip_payment_method,name="roundtrip_payment_method"),
    path("roundtrip_make_payment",views.roundtrip_make_payment,name="roundtrip_make_payment")
]