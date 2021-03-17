from django.urls import path
from . import views

urlpatterns = [
    path("view_payment_history",views.view_payment_history,name="view_payment_history"),
    path("view_ticket",views.view_ticket,name="view_ticket"),
    path("payment_method",views.payment_method,name="payment_method"),
    path("make_payment",views.make_payment,name="make_payment"),
    path("flight<int:flight_id>,<int:travellers>,<str:cls>",views.payment,name="flight"),
    path("cancel_ticket_form<int:ticket_id>",views.cancel_ticket_form,name="cancel_ticket_form"),
    path("cancel_ticket",views.cancel_ticket,name="cancel_ticket"),
    path("roundtrip_flight<int:flight_id1>,<int:flight_id2>,<int:travellers>,<str:cls>",views.roundtrip_payment,name="roundtrip_flight"),
    path("roundtrip_payment_method",views.roundtrip_payment_method,name="roundtrip_payment_method"),
    path("roundtrip_make_payment",views.roundtrip_make_payment,name="roundtrip_make_payment"),
    path("error",views.cancel_ticket_error,name="cancel_ticket_errro")
]