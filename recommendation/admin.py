from django.contrib import admin

# Register your models here.
from recommendation.models import Customer

#admin.site.register(Customer)

class CustomerAdmin(admin.ModelAdmin):
	list_display= ('customer_id','antivirus_version','antivirus_expiry_date','office_expiry_date','office_data','in_home_hardware_service_expiry_date','warranty_expiry_date','sys_model','purchase_data')
	list_filter=('antivirus_expiry_date','office_expiry_date','in_home_hardware_service_expiry_date','warranty_expiry_date')
admin.site.register(Customer,CustomerAdmin)
