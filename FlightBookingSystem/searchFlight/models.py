from django.db import models

# Create your models here.

class flight_details(models.Model):
    class Meta:
        unique_together = (('flight_no', 'departure_time', 'date'),)
        
    source = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    date = models.DateField()
    capacity = models.IntegerField()
    economy_price = models.IntegerField()
    business_price = models.IntegerField()
    first_class_price = models.IntegerField()
    departure_time = models.TimeField()
    arrival_time = models.TimeField()
    flight_no = models.CharField(max_length=10)
    company = models.CharField(max_length=20)