import pandas as pd
import datetime

def district():		
	data= pd.read_csv('Dataset_Cases - Sheet1.csv')
	mumbai=data['Mumbai']
	pune=data['Pune']
	nagpur=data['Nagpur']
	nashik=data['Nashik']
	thane=data['Thane']
	today = datetime.date.today()
	date=pd.date_range(start='5/1/2020', end=today)
	start = datetime.datetime.strptime("1-05-2020", "%d-%m-%Y")
	end = datetime.datetime.strptime("17-05-2020", "%d-%m-%Y")
	date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]
	dates=[]
	for date in date_generated:
		dates.append(date.strftime("%d-%m-%Y"))

	return dates,mumbai,pune,nashik,nagpur,thane







