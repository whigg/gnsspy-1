import sys
import numpy as np
import datetime
import http.client

def obsFileName(station, date, zipped = False):
	Station = station # station name
	doy = datetime2doy(date, string = True) # for RINEX data names 
	if len(doy) == 1:
		rinexFile = Station + doy + "0." + str(date.year)[-2:] + "o"
	elif len(doy) == 2:
		rinexFile = Station + doy + "0." + str(date.year)[-2:] + "o"
	else:
		rinexFile = Station + doy + "0." + str(date.year)[-2:] + "o"
	
	if zipped == True:
		rinexFile = rinexFile + ".Z"
	
	return rinexFile

def sp3FileName(epoch):
	now = datetime.date.today() # today's date
	timeDif = now - epoch # time difference between rinex epoch and today

	if timeDif.days == 0:
		raise Warning("IGS orbit files are not released for", epoch.ctime())
		sys.exit("Exiting...")
	elif 0 < timeDif.days < 13:
		raise Warning("IGS final orbit file is not released for", epoch.ctime(), "\nDownloading IGS Rapid orbit file...")
		prefix = 'igr' # sp3 file name
	else:
		prefix = 'igs' # sp3 file name

	gpsWeek, gpsWeekday = gpsweekday(epoch, Datetime = True) # GPS week
	sp3File = prefix + str(gpsWeekday) + ".sp3"
	return sp3File

def clockFileName(epoch, interval):
	now = datetime.date.today() # today's date
	timeDif = now - epoch # time difference between rinex epoch and today

	if timeDif.days == 0:
		raise Warning("IGS clock files are not released for", epoch.ctime())
		sys.exit("Exiting...")
	elif 0 < timeDif.days < 13:
		prefix = 'igr' # clock file name
	else:
		prefix = 'cod' # clock file name

	if interval < 30:
		extension = '.clk_05s'
	else:
		extension = '.clk'

	gpsWeek, gpsWeekday = gpsweekday(epoch, Datetime = True) # GPS week
	clockFile = prefix + str(gpsWeekday) + extension
	return clockFile