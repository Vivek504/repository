from django.db import models
import datetime
# Create your models here.

class paymentHistory(models.Model):
    username=models.CharField(max_length=50)
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    mobile_no=models.CharField(max_length=10)
    payment_method=models.CharField(max_length=20)
    payment_date=models.DateTimeField(auto_now_add=True,blank=True)
    
class ticket_details(models.Model):
    username=models.CharField(max_length=50)
    flight_id=models.IntegerField()
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    price=models.CharField(max_length=10)
    company=models.CharField(max_length=20)
    flight_no=models.CharField(max_length=10)
    departure_time=models.CharField(max_length=15)
    arrival_time=models.CharField(max_length=15)
    source=models.CharField(max_length=50)
    destination=models.CharField(max_length=50)
    departure_date=models.CharField(max_length=15)
    travellers=models.CharField(max_length=4)