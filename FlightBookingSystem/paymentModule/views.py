from django.shortcuts import render,redirect
from .models import paymentHistory
from .models import ticket_details
from searchFlight.models import flight_details
from django.conf import settings 
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.template.loader import render_to_string

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
        p=paymentHistory(username=current_user,first_name=first_name,last_name=last_name,mobile_no=mobile_no,payment_method=payment_method)
        p.save()
        ticket=ticket_details(username=current_user,flight_id=flight_id,first_name=first_name,last_name=last_name,price=price,company=flight.company,flight_no=flight.flight_no,
        departure_time=flight.departure_time,arrival_time=flight.arrival_time,source=flight.source,destination=flight.destination,departure_date=flight.date,
        travellers=travellers)
        ticket.save()
        ticket_id=ticket.id
        confirm_seat=flight.capacity - travellers
        seat=flight_details.objects.get(id=flight_id)
        seat.capacity=confirm_seat
        seat.save()
        
        subject = 'Thank you'
        # message = f'Ticket reservation is done successfully.Flight details are as follows:Flight Number:{{flight.flight_no}}'
        message = render_to_string('mail_file.html',{'flight':flight,'cls':cls,'travellers':travellers})
        email_from = settings.EMAIL_HOST_USER 
        recipient_list = [email, ] 
        send_mail( subject, message, email_from, recipient_list ) 
        return redirect('home')
    else:
        return render(request,"home.html")

def view_payment_history(request):
    current_user=request.user
    data=paymentHistory.objects.all().filter(username=current_user)
    return render(request,"view_payment_history.html",{'data':data})
    
def view_ticket(request):
    current_user=request.user
    data=ticket_details.objects.all().filter(username=current_user)
    return render(request,"view_ticket.html",{'data':data})

def cancel_ticket_form(request,ticket_id):
    request.session['ticket_id']=ticket_id
    return render(request,"cancel_ticket.html")

def cancel_ticket(request):
    if request.method == 'POST':
        username=request.POST.get('username','')
        password=request.POST.get('password','')
        ticket_id=request.session['ticket_id']
        if username==request.user.username:    
            user=auth.authenticate(username=username,password=password)
            if user is not None:
                ticket_ids=ticket_details.objects.all().filter(username=request.user)
                for ticket in ticket_ids:
                    if ticket.id==ticket_id:
                        ticket=ticket_details.objects.get(id=ticket_id)
                        ticket.delete()
                        return redirect('home')
                    else:
                        messages.info(request,'Somethong went wrong!!')
                        return render(request,"cancel_ticket_error.html",{'ticket_id':ticket_id})    
            else:
                messages.info(request,'Invalid username or password')
                return render(request,"cancel_ticket_error.html",{'ticket_id':ticket_id})    
        else:
            messages.info(request,'Invalid username or password')
            return render(request,"cancel_ticket_error.html",{'ticket_id':ticket_id})
    else:
        return redirect("login")

def cancel_ticket_error(request):
    return render(request,"cancel_ticket_error.html")

def roundtrip_payment(request,flight_id1,flight_id2,travellers,cls):
    going_flight=flight_details.objects.get(id=flight_id1)
    return_flight=flight_details.objects.get(id=flight_id2)
    request.session['flight_id1']=flight_id1
    request.session['flight_id2']=flight_id2
    request.session['cls']=cls
    request.session['travellers']=travellers
    if cls=="Economy":
        price=(going_flight.economy_price*travellers)+(return_flight.economy_price*travellers)
    elif cls=="Business":
        price=(going_flight.business_price*travellers)+(return_flight.business_price*travellers)
    else:
        price=(going_flight.first_class_price*travellers)+(return_flight.first_class_price*travellers)
    return render(request,"roundtrip_payment.html",{'flight1':going_flight,'flight2':return_flight,'price':price,'travellers':travellers})

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
        p=paymentHistory(username=current_user,first_name=first_name,last_name=last_name,mobile_no=mobile_no,payment_method=payment_method)
        p.save()
        going_ticket=ticket_details(username=current_user,flight_id=flight_id1,first_name=first_name,last_name=last_name,price=price1,company=flight1.company,flight_no=flight1.flight_no,
        departure_time=flight1.departure_time,arrival_time=flight1.arrival_time,source=flight1.source,destination=flight1.destination,departure_date=flight1.date,
        travellers=travellers)
        going_ticket.save()
        return_ticket=ticket_details(username=current_user,flight_id=flight_id2,first_name=first_name,last_name=last_name,price=price2,company=flight2.company,flight_no=flight2.flight_no,
        departure_time=flight2.departure_time,arrival_time=flight2.arrival_time,source=flight2.source,destination=flight2.destination,departure_date=flight2.date,
        travellers=travellers)
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
        message = f'Ticket reservation is done successfully.{going_ticket_id} and {return_ticket_id} '
        email_from = settings.EMAIL_HOST_USER 
        recipient_list = [email, ] 
        send_mail( subject, message, email_from, recipient_list ) 
        return redirect('home')
    else:
        return render(request,"home.html")