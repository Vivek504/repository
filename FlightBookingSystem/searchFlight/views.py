from django.shortcuts import render,redirect
from .models import flight_details
from datetime import date
from datetime import datetime
# Create your views here.

def home(request):
    return render(request,'home.html')
   
def onewayTrip(request):
    if request.method == 'POST':
        source=request.POST['from']
        destination=request.POST['to']
        dep_date=request.POST['depdate']
        travellers=request.POST['travellers']
        cls=request.POST['class']
        current_date=date.today()
        current_time=datetime.now().time()
        data=flight_details.objects.all().filter(source=source, destination=destination, date=dep_date)
        return render(request, "oneway_flight_details.html", {'data':data, 'cls':cls, 'travellers':travellers,'source':source,'destination':destination,'current_date':current_date,'current_time':current_time})
    else:
        return render(request,'home.html')
        
def roundTrip(request):
    if request.method == 'POST':
        source=request.POST['from']
        destination=request.POST['to']
        dep_date=request.POST['depdate']
        ret_date=request.POST['retdate']
        travellers=request.POST['travellers']
        cls=request.POST['class']
        current_date=date.today()
        current_time=datetime.now().time()
        data1=flight_details.objects.all().filter(source=source, destination=destination, date=dep_date)
        data2=flight_details.objects.all().filter(source=destination, destination=source, date=ret_date)
        return render(request, "roundtrip_flight_details.html", {'data1':data1,'data2':data2, 'cls':cls, 'travellers':travellers, 'ret_date':ret_date,'source':source,'destination':destination,'current_date':current_date,'current_time':current_time})
    else:
        return render(request,'home.html')
        