def getTimescale(ts, now):
	year = int(now.strftime("%Y"))
	month = int(now.strftime("%m"))
	day = int(now.strftime("%d"))
	hour = int(now.strftime("%H"))
	minute = int(now.strftime("%M"))
	second = int(now.strftime("%S"))
	t = ts.utc(year, month, day, hour, minute, second)
	return t
