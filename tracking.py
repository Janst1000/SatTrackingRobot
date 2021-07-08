import csv

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