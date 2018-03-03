import sys
import numpy as np
import datetime
import http.client

def isfloat(value):
	""" To check if any value can be converted to float """
	try:
		float(value)
		return True
	except ValueError:
		return False
			
def isint(value):
	""" To check if any value can be converted to integer """
	try:
		int(value)
		return True
	except ValueError:
		return False

def check_internet():
    conn = http.client.HTTPConnection("www.google.com", timeout=5)
    try:
        conn.request("HEAD", "/")
        conn.close()
        return True
    except:
        conn.close()
        return False