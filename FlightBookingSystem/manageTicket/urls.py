from django.urls import path
from . import views

urlpatterns = [
    path("view_ticket",views.view_ticket,name="view_ticket"),
    path("cancel_ticket",views.cancel_ticket,name="cancel_ticket"),
    path("cancel_ticket_form",views.cancel_ticket_form,name="cancel_ticket_form"),
]