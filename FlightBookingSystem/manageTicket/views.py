from django.shortcuts import render,redirect
from .models import ticket_details
from searchFlight.models import flight_details
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.template.loader import render_to_string
from datetime import date

# Create your views here.

def view_ticket(request):
    current_user=request.user
    data=ticket_details.objects.all().filter(username=current_user).order_by('departure_date').reverse()
    count=ticket_details.objects.all().filter(username=current_user).count()
    if count == 0:
        messages.info(request,"No Tickets Found.")
    current_date=date.today()
    return render(request,"view_ticket.html",{'data':data,'current_date':current_date})

def cancel_ticket_form(request):
    request.session['ticket_id']=request.POST.get('ticket_id','')
    request.session['flight_id']=request.POST.get('flight_id','')
    request.session['travellers']=request.POST.get('travellers','')
    request.session['cls']=request.POST.get('cls','')
    return render(request,"cancel_ticket.html")

def cancel_ticket(request):
    if request.method == 'POST':
        username=request.POST.get('username','')
        password=request.POST.get('password','')
        ticket_id=request.session['ticket_id']
        flight_id=request.session['flight_id']
        travellers=request.session['travellers']
        cls=request.session['cls']
        if username==request.user.username:    
            user=auth.authenticate(username=username,password=password)
            if user is not None:
                flight=flight_details.objects.get(id=flight_id)
                flight.capacity=flight.capacity + int(travellers)
                flight.save()
                ticket=ticket_details.objects.get(id=ticket_id)
                ticket.delete()
                subject = 'Ticket is Cancelled'
                message = render_to_string('cancel_ticket_mail.html',{'flight':flight,'cls':cls,'travellers':travellers})
                email_from = settings.EMAIL_HOST_USER 
                recipient_list = [request.user.email, ] 
                send_mail( subject, message, email_from, recipient_list )
                messages.info(request,'Your Reservation is cancelled successfully.')
                return redirect('home')
            else:
                messages.info(request,'Invalid username or password')
                return render(request,"cancel_ticket.html") 
        else:
            messages.info(request,'Invalid username or password')
            return render(request,"cancel_ticket.html")
    else:
        return redirect("login")