import numpy as np

__all__ = ["ell2cart", "cart2ell"]

class ellipsoid:
	def __init__(self,a ,e2):
		self.a = a
		self.e2 = e2
a = 6378137.0 # GRS80 semi-major axis in meters
e2 = 0.00669438002290 # firs eccentricity
grs80 = ellipsoid(a,e2)
	
def ell2cart(lat, lon, h, ellipsoid):
	"""  This funcion converts geodetic coordinates to cartesian coordinates """
	lat = lat * np.pi / 180 # in radians
	lon = lon * np.pi / 180 # in radians
	N = ellipsoid.a / np.sqrt(1-ellipsoid.e2 * np.sin(lat)**2) # radius of curvature in the prime vertical
	x = (N + h) * np.cos(lat) * np.cos(lon)
	y = (N + h) * np.cos(lat) * np.sin(lon)
	z = ((1-ellipsoid.e2) * N + h) * np.sin(lat)
	return x,y,z

def cart2ell(cartCoor):
	semimajor = 6378137.0 #semimajor axis of wgs84 elipsoid in meter
	semiminor = 6356752.314 #semiminor axis of wgs84 elipsoid in meter
	flattening = 1-(semiminor/semimajor) #flattening of wgs 84 elipsoid
	ecc = 2*flattening-flattening**2

	longitude = np.arctan2(cartCoor[1], cartCoor[0])
	p = np.sqrt(cartCoor[0]**2+cartCoor[1]**2)
	initlat = np.arctan2(cartCoor[2], ((1-ecc)*p))

	precision = 1e-16
	while True:
		initN = semimajor/np.sqrt(1-(ecc*(np.sin(initlat)**2)))
		inith = (p/np.cos(initlat))-initN
		latitude = np.arctan2(cartCoor[2],(1-ecc*(initN/(initN+inith)))*p)
		if np.abs(initlat - latitude) > precision:
			initlat = latitude
		else:
			latitude = latitude
			h = inith
			break

	ellCoor = [np.degrees(latitude), np.degrees(longitude), h]
	return ellCoor
