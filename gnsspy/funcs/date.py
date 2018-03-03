import sys
import numpy as np
import datetime
import http.client

def gpsweekday(date, Datetime = False):
	start = datetime.date(year= 1980, month= 1, day =6)
	if Datetime == True:
		date = date
	else:
		date = datetime.date(year= int(date[-4:]), month= int(date[-7:-5]), day = int(date[:2]))
	diff = date-start
	diff = diff.days
	week = int(diff/7)
	day = diff%7
	gpswday = int(str(week)+str(day))
	return week, gpswday

def gpswdtodate(gpsweekday):
	week = int(gpsweekday[:4])
	totalday = week*7 + int(gpsweekday[4])
	start = datetime.datetime(year= 1980, month= 1, day =6)
	day = start + datetime.timedelta(days=totalday)
	day = day.date()
	return day

def jday(date):
	""" This function calculates Julian day of a given date as DD MM YYYY"""
	userD = date
	#convert str to int
	Y = int(userD[-4:])
	M = int(userD[3:5])
	if M == 1 or M == 2:
		M += 12
		Y += -1
	#calculate JD of input time
	A = int(Y/100)
	B = int(A/4)
	C = 2-A+B
	D = int(userD[:2])
	E = int(365.25*(Y+4716))
	F = int(30.6001*(M+1))
	Jd = C+D+E+F-1524.5
	return Jd

def Jday2date(JDay):
	MJd = JDay - 2400000.5 #calculate modified Julian date
	start = datetime.datetime(year= 1858, month = 11, day = 17, hour=0, minute=0, second=0)
	date = start + datetime.timedelta(days=MJd)
	return date

def doy(date):
	""" This function is made for calculate the GPS day of year for the date which inputs the user  """
	year=int(date[-4:])
	month=int(date[-7:-5])
	day=int(date[-10:-8])
	doy=((month-1)*(30))+day
	if year%4!=0:
		if month == 1 or month == 4 or month == 5:
			doy=doy
		elif month == 2 or month == 6 or month == 7:
			doy=doy+1
		elif month == 3:
			doy=doy-1
		elif month == 8:
			doy=doy+2
		elif month == 9 or month == 10:
			doy=doy+3
		elif month ==11 or month == 12:
			doy=doy+4
	#for leap year
	else:
		if month ==1 or month ==3:
			doy=doy
		elif month ==2 or month == 4 or month == 5:
			doy=doy+1
		elif month ==6 or month == 7:
			doy=doy+2
		elif month ==8:
			doy=doy+3
		elif month ==9 or month == 10:
			doy=doy+4
		elif month ==11 or month == 12:
			doy=doy+5
	return doy

def doy2date(ObsFile):
	if int(ObsFile[-3:-1]) < 80:
		year = int('20'+ObsFile[-3:-1])
	else:
		year = int('19'+ObsFile[-3:-1])

	start = datetime.datetime(year= year, month = 1,  day =1)
	date = start + datetime.timedelta(days=int(ObsFile[4:7]))-datetime.timedelta(days=1)
	date = date.date()
	return date

def datetime2doy(date, string = False):
	start = datetime.datetime(year= date.year, month = 1,  day =1)
	doy = date - start + datetime.timedelta(days = 1)
	doy = doy.days
	if string == True:
		doy = str(doy)
		if len(doy) == 1:
			doy = "00" + doy 
		elif len(doy) == 2:
			doy = "0" + doy
		else:
			doy = doy 
	return doy