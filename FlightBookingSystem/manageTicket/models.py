from django.db import models
import datetime
# Create your models here.

class ticket_details(models.Model):
    username=models.CharField(max_length=50)
    flight_id=models.IntegerField()
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    price=models.CharField(max_length=10)
    company=models.CharField(max_length=20)
    flight_no=models.CharField(max_length=10)
    departure_time=models.TimeField()
    arrival_time=models.TimeField()
    source=models.CharField(max_length=50)
    destination=models.CharField(max_length=50)
    departure_date=models.DateField()
    arrival_date=models.DateField()
    cls=models.CharField(max_length=20)
    travellers=models.IntegerField()