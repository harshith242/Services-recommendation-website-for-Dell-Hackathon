from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns= [
	path('',views.home,name='home'),
    path('customer/',views.customer,name='customer'),
    path('administrator/',views.administrator,name='administrator'),
    path('contact/',views.contact,name='contact'),
    path('admin_login/',views.admin_login,name='admin_login'),
    path('about/',views.about,name='about'),
    path('customer/<int:my_id>',views.CustomerDetailView,name='customer-detail')
]