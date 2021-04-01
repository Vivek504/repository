from django.shortcuts import render,redirect
from .models import paymentHistory
from manageTicket.models import ticket_details
from searchFlight.models import flight_details
from django.conf import settings 
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.template.loader import render_to_string
from datetime import date

# Create your views here.

def payment(request,flight_id,travellers,cls):
    flight=flight_details.objects.get(id=flight_id)
    request.session['flight_id']=flight_id
    request.session['cls']=cls
    request.session['travellers']=travellers
    if cls=="Economy":
        price=flight.economy_price*travellers
    elif cls=="Business":
        price=flight.business_price*travellers
    else:
        price=flight.first_class_price*travellers
    return render(request,"payment.html",{'flight':flight,'price':price,'travellers':travellers,'cls':cls})
    
def payment_method(request):
    if request.method == 'POST':
        current_user=request.user
        first_name=request.POST.get('fname','')
        last_name=request.POST.get('lname','')
        mobile_no=request.POST.get('mobno','')
        email=request.POST.get('email','')
        payment_method=request.POST.get('paymethod','')
        request.session['mobile_no']=mobile_no
        request.session['email']=email
        request.session['payment_method']=payment_method
        request.session['first_name']=first_name
        request.session['last_name']=last_name
        if payment_method=='debit':
            return render(request,"debit.html")
        elif payment_method=='credit':
            return render(request,"credit.html")

def make_payment(request):
    if request.method == 'POST':
        current_user=request.user
        first_name=request.session['first_name']
        last_name=request.session['last_name']
        mobile_no=request.session['mobile_no']
        email=request.session['email']
        payment_method=request.session['payment_method']
        flight_id=request.session['flight_id']
        flight=flight_details.objects.get(id=flight_id)
        cls=request.session['cls']
        travellers=request.session['travellers']
        if cls=="Economy":
            price=flight.economy_price*travellers
        elif cls=="Business":
            price=flight.business_price*travellers
        else:
            price=flight.first_class_price*travellers
        p=paymentHistory(username=current_user,first_name=first_name,last_name=last_name,mobile_no=mobile_no,email=email,payment_method=payment_method)
        p.save()
        ticket=ticket_details(username=current_user,flight_id=flight_id,first_name=first_name,last_name=last_name,price=price,company=flight.company,flight_no=flight.flight_no,
        departure_time=flight.departure_time,arrival_time=flight.arrival_time,source=flight.source,destination=flight.destination,departure_date=flight.date,
        arrival_date=flight.arrival_date,cls=cls,travellers=travellers)
        ticket.save()
        ticket_id=ticket.id
        confirm_seat=flight.capacity - travellers
        seat=flight_details.objects.get(id=flight_id)
        seat.capacity=confirm_seat
        seat.save()
        
        subject = 'Thank you'
        message = render_to_string('oneway_mail.html',{'flight':flight,'cls':cls,'travellers':travellers})
        email_from = settings.EMAIL_HOST_USER 
        recipient_list = [email, ] 
        send_mail( subject, message, email_from, recipient_list ) 
        return redirect('home')
    else:
        return render(request,"home.html")

def view_payment_history(request):
    current_user=request.user
    data=paymentHistory.objects.all().filter(username=current_user)
    count=paymentHistory.objects.all().filter(username=current_user).count()
    if count == 0:
        messages.info(request,"No Payment History Found.")
    return render(request,"view_payment_history.html",{'data':data})

def roundtrip_payment(request,flight_id1,flight_id2,travellers,cls):
    going_flight=flight_details.objects.get(id=flight_id1)
    return_flight=flight_details.objects.get(id=flight_id2)
    request.session['flight_id1']=flight_id1
    request.session['flight_id2']=flight_id2
    request.session['cls']=cls
    request.session['travellers']=travellers
    if cls=="Economy":
        price1=going_flight.economy_price*travellers
        price2=return_flight.economy_price*travellers
    elif cls=="Business":
        price1=going_flight.business_price*travellers
        price2=return_flight.business_price*travellers
    else:
        price1=going_flight.first_class_price*travellers
        price2=return_flight.first_class_price*travellers
    return render(request,"roundtrip_payment.html",{'flight1':going_flight,'flight2':return_flight,'price1':price1,'price2':price2,'travellers':travellers})

def roundtrip_payment_method(request):
    if request.method == 'POST':
        current_user=request.user
        first_name=request.POST.get('fname','')
        last_name=request.POST.get('lname','')
        mobile_no=request.POST.get('mobno','')
        email=request.POST.get('email','')
        payment_method=request.POST.get('paymethod','')
        request.session['mobile_no']=mobile_no
        request.session['email']=email
        request.session['payment_method']=payment_method
        request.session['first_name']=first_name
        request.session['last_name']=last_name
        if payment_method=='credit':
            return render(request,"roundtrip_credit.html")
        elif payment_method=='debit':
            return render(request,"roundtrip_debit.html")

def roundtrip_make_payment(request):
    if request.method == 'POST':
        current_user=request.user
        first_name=request.session['first_name']
        last_name=request.session['last_name']
        mobile_no=request.session['mobile_no']
        email=request.session['email']
        payment_method=request.session['payment_method']
        flight_id1=request.session['flight_id1']
        flight_id2=request.session['flight_id2']
        flight1=flight_details.objects.get(id=flight_id1)
        flight2=flight_details.objects.get(id=flight_id2)
        cls=request.session['cls']
        travellers=request.session['travellers']
        if cls=="Economy":
            price1=flight1.economy_price*travellers
            price2=flight2.economy_price*travellers
        elif cls=="Business":
            price1=flight1.business_price*travellers
            price2=flight2.business_price*travellers
        else:
            price1=flight1.first_class_price*travellers
            price2=flight2.first_class_price*travellers
        price=price1+price2    
        p=paymentHistory(username=current_user,first_name=first_name,last_name=last_name,mobile_no=mobile_no,email=email,payment_method=payment_method)
        p.save()
        going_ticket=ticket_details(username=current_user,flight_id=flight_id1,first_name=first_name,last_name=last_name,price=price1,company=flight1.company,flight_no=flight1.flight_no,
        departure_time=flight1.departure_time,arrival_time=flight1.arrival_time,source=flight1.source,destination=flight1.destination,departure_date=flight1.date,arrival_date=flight1.arrival_date,
        cls=cls,travellers=travellers)
        going_ticket.save()
        return_ticket=ticket_details(username=current_user,flight_id=flight_id2,first_name=first_name,last_name=last_name,price=price2,company=flight2.company,flight_no=flight2.flight_no,
        departure_time=flight2.departure_time,arrival_time=flight2.arrival_time,source=flight2.source,destination=flight2.destination,departure_date=flight2.date,arrival_date=flight2.arrival_date,
        cls=cls,travellers=travellers)
        return_ticket.save()
        going_ticket_id=going_ticket.id
        return_ticket_id=return_ticket.id
        confirm_seat1=flight1.capacity - travellers
        confirm_seat2=flight2.capacity - travellers
        seat1=flight_details.objects.get(id=flight_id1)
        seat1.capacity=confirm_seat1
        seat1.save()
        seat2=flight_details.objects.get(id=flight_id2)
        seat2.capacity=confirm_seat2
        seat2.save()
        subject = 'Thank you'
        message = render_to_string('roundtrip_mail.html',{'flight1':flight1,'flight2':flight2,'cls':cls,'travellers':travellers})
        email_from = settings.EMAIL_HOST_USER 
        recipient_list = [email, ] 
        send_mail( subject, message, email_from, recipient_list ) 
        return redirect('home')
    else:
        return render(request,"home.html")