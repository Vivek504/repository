from django.db import models
import datetime
# Create your models here.

class paymentHistory(models.Model):
    username=models.CharField(max_length=50)
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    mobile_no=models.CharField(max_length=10)
    email=models.CharField(max_length=50)
    payment_method=models.CharField(max_length=20)
    payment_date=models.DateTimeField(auto_now_add=True,blank=True)