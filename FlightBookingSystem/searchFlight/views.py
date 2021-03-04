from django.shortcuts import render
from .models import flight_details
# Create your views here.

def home(request):
    if request.method == 'POST':
        source=request.POST['from']
        destination=request.POST['to']
        dep_date=request.POST['depdate']
        travellers=request.POST['travellers']
        cls=request.POST['class']
        
        data=flight_details.objects.all().filter(source=source, destination=destination, date=dep_date)
       
        
        return render(request, "flight_details.html", {'data':data, 'cls':cls, 'travellers':travellers})
        
        
    else:
        return render(request,'home.html')
   
def flights(request):
    return render(request,'flight_details.html')