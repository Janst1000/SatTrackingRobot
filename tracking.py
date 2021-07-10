import csv
from skyfield.api import wgs84

def getTimescale(ts, now):
	year = int(now.strftime("%Y"))
	month = int(now.strftime("%m"))
	day = int(now.strftime("%d"))
	hour = int(now.strftime("%H"))
	minute = int(now.strftime("%M"))
	second = int(now.strftime("%S"))
	t = ts.utc(year, month, day, hour, minute, second)
	return t

def saveLocation(name, lat, lon):
	row = [name, lat, lon, elv]
	# open the file in the write mode
	with open('location.csv', 'w') as f:
		# create the csv writer
		writer = csv.writer(f)

		# write a row to the csv file
		writer.writerow(row)

def loadLocation():
	# open file to read from
	with open('location.csv', 'r') as f:
		reader = csv.reader(f)
		#reads the first line of the location csv file
		row = next(reader)
	# saving the read data into variables and returning it as a usuable
	# wgs84 location
	lat = float(row[1])
	lon = float(row[2])
	elv = float(row[3])
	return wgs84.latlon(lat, lon, elv)
