from django.db import models
from django.urls import reverse
from datetime import date
# Create your models here.

class Customer(models.Model):
	customer_id=models.IntegerField()
	antivirus_version=models.IntegerField()
	antivirus_expiry_date=models.DateField(default=date.today)
	office_expiry_date=models.DateField(default=date.today)
	in_home_hardware_service_expiry_date=models.DateField(default=date.today)
	warranty_expiry_date=models.DateField(default=date.today)
	office_data=models.CharField(max_length=30,default=None)
	sys_model=models.CharField(max_length=30,default=None)
	purchase_data=models.DateField(default=date.today)
	
	def get_absolute_url(self):
		return reverse('customer-detail',args=[str(self.id)])

