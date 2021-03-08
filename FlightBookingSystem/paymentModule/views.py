from django.shortcuts import render,redirect
from .models import paymentHistory
from .models import ticket_details
from searchFlight.models import flight_details

# Create your views here.

def payment(request,flight_id,travellers,cls):
    flight=flight_details.objects.get(id=flight_id)
    request.session['flight_id']=flight_id
    request.session['cls']=cls
    request.session['travellers']=travellers
    if cls=="economy":
        price=flight.economy_price*travellers
    elif cls=="business":
        price=flight.business_price*travellers
    else:
        price=flight.first_class_price*travellers
    return render(request,"payment.html",{'flight':flight,'price':price,'travellers':travellers})
    
def payment_method(request):
    if request.method == 'POST':
        current_user=request.user
        first_name=request.POST.get('fname','')
        last_name=request.POST.get('lname','')
        mobile_no=request.POST.get('mobno','')
        payment_method=request.POST.get('paymethod','')
        request.session['mobile_no']=mobile_no
        request.session['payment_method']=payment_method
        request.session['first_name']=first_name
        request.session['last_name']=last_name
        return render(request,"make_payment.html")

def make_payment(request):
    if request.method == 'POST':
        current_user=request.user
        first_name=request.session['first_name']
        last_name=request.session['last_name']
        mobile_no=request.session['mobile_no']
        payment_method=request.session['payment_method']
        flight_id=request.session['flight_id']
        flight=flight_details.objects.get(id=flight_id)
        cls=request.session['cls']
        travellers=request.session['travellers']
        if cls=="economy":
            price=flight.economy_price*travellers
        elif cls=="business":
            price=flight.business_price*travellers
        else:
            price=flight.first_class_price*travellers
        p=paymentHistory(username=current_user,first_name=first_name,last_name=last_name,mobile_no=mobile_no,payment_method=payment_method)
        p.save()
        ticket=ticket_details(username=current_user,flight_id=flight_id,first_name=first_name,last_name=last_name,price=price,company=flight.company,flight_no=flight.flight_no,
        departure_time=flight.departure_time,arrival_time=flight.arrival_time,source=flight.source,destination=flight.destination,departure_date=flight.date,
        travellers=travellers)
        ticket.save()
        confirm_seat=flight.capacity - travellers
        seat=flight_details.objects.get(id=flight_id)
        seat.capacity=confirm_seat
        seat.save()
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