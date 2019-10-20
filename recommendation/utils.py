from datetime import date

def hello(x):
	d_anti_virus = x.antivirus_expiry_date
	d1 = date.today()
	rec_anti=[]
	delta = d_anti_virus - d1
	print(delta.days)
	if(delta.days<60):
		print ("hello")
		if(x.antivirus_version<5):
			print(1)
			rec_anti=['Version 5','Version 6','Version 7']
		elif (x.antivirus_version==6):
			rec_anti=[6,7]
		else:
			rec_anti=[7]
	print(rec_anti)
	return rec_anti
	
