from django.shortcuts import render
from recommendation.models import Customer
from recommendation.utils import hello
from django.shortcuts import get_object_or_404
# Create your views here.
class Recommendation():
	anti=[]


def home(request):
	return render(request,'home.html',{})
def customer(request):
	obj=None
	result=None
	if request.GET.get('ref_id'):
		result=Recommendation()
		ref_id=request.GET.get('ref_id')
		obj=get_object_or_404(Customer,customer_id=ref_id)
		result.anti=hello(obj)
	context={
		'object':obj,
		'result':result
	}
	return render(request,'customer.html',context)

def administrator(request):
	change={
		'value':'0'
	}
	if request.GET.get('username')!=None:
		username=request.GET.get('username')
		password=request.GET.get('password')
		if(username=='test' ):
			if(password=='test1234'):
				change['value']='1'
				return render(request,'admin_login.html',{})
			else:
				change['value']='2'
		else:
			change['value']='2'

	print(change['value'])		
	return render(request,'admin.html',change)

def admin_login(request):
	return render(request,'admin_login.html',{})

def contact(request):
	return render(request,'contact.html',{})

def CustomerDetailView(request,my_id):
	customer=Customer.objects.get(id=my_id)
	context={
	'customer':customer
	}
	return render(request,'customer_detail.html',context)

def about(request):
	return render(request,'about.html',{})