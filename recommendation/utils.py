from datetime import date

def hello(x):
	d_anti_virus = x.antivirus_expiry_date
	d1 = date.today()
	rec_anti=[]
	delta = d_anti_virus - d1
	print(delta.days)
	if(delta.days<60):
		print ("hello")
		if(x.antivirus_version<=5):
			print(1)
			rec_anti=['Version 5','Version 6','Version 7']
		elif (x.antivirus_version==6):
			rec_anti=['Version 6','Version 7']
		else:
			rec_anti=['Version 7']
	elif(x.antivirus_version==7):
		rec_anti=['upto date']
	else:
		rec_anti=['needs update']
	print(rec_anti)
	return rec_anti

def office(x):
	office=[]
	if(x.office_data=='Home and Student'):
		office=['Home and Business','Professional']
	elif(x.office_data=='Home and Business'):
		office=['Professional']
	elif(x.office_data=='Professional'):
		office=['highest Version']
	else:
		date_office=x.office_expiry_date
		d1=date.today()
		delta=date_office -d1
		if ((delta.days<60) or None):
			office=['Home and Student(1year)','Home and Student','Home and Business','Professional']
		else:
			office=[]
	return office

def hardware(x):
	hardware=[]
	date_hardware=x.in_home_hardware_service_expiry_date
	d1=date.today()
	delta=date_hardware-d1
	if (delta.days<60):
		hardware=['1 year hardware service','2 years hardware service','3 years hardware service']
	else:
		string=str(delta.days)+' '+'days left'
		hardware=[string]
	return hardware

def model(x):
	model=[]
	data=x.sys_model
	if (data=='Gaming'):
		model=['Gaming Mouse','Mechanical Keyboard','Headset']
	elif(data=='Work'):
		model=['Mouse','USB','Web Cam','Sleeve Bag']
	elif(data=='Home'):
		model=['Mouse','Keyboard','Hard Disk']
	else:
		model=['No available info']
	return model


