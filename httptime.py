'''TODO:
-More timestamp objects, and maybe better names
-Add date functions
-Maybe break time and date functions into separate files
-Documentation
-Examples'''

import re
import datetime
import calendar

# If your timestamp looks like 06/Dec/2011:13:12:48

class DateSlashTimeColon(object):

	def __init__(self, timestamp):
		self.timestamp = timestamp

	# Splits up timestamp
	def date_and_time(self):
		date = re.search(r'([0-9]{2}/\w{3}/[0-9]{4})', self.timestamp)
		time = re.search(r':([0-9]{2}:[0-9]{2}:[0-9]{2})', self.timestamp)
		return date.group(0), time.group(1)

	# Get separate date pieces - returns as str
	def date_pieces(self):
		date, time = self.date_and_time()
		day, month, year = date.split('/')
		return day, month, year

	# Get separate time pieces - returns as str
	def time_pieces(self):
		date, time = self.date_and_time()
		hour, minute, second = time.split(':')
		return hour, minute, second

# Time functions

# Converts time from timestamp to seconds

 def time_to_seconds(time):
    h, m, s = [int(i) for i in time.split(':')]
    return (3600 * h) + (60 * m) + s

# Converts seconds to time -- don't think I need this
#def seconds_to_time(seconds):
#	return datetime.timedelta(seconds = sec)

# Calculates time difference
def calculate_time_difference(time1, time2):
	sec = time_to_seconds(time2) - time_to_seconds(time1)
	return datetime.timedelta(seconds = abs(sec))

# Calculates time addition
def calculate_time_addition(time1, time2):
	sec = time_to_seconds(time2) + time_to_seconds(time1)
	return datetime.timedelta(seconds = sec)

# Date functions

# Get the month number
def month_number(month):
	month = month[0:3]
	cal = dict((v,k) for k,v in enumerate(calendar.month_abbr))
	if month in cal.keys():
		return int(cal[month])

# Find number of days between two dates
#def day_difference(day1, day2):


# Find number of months between two months
def month_difference(month1, month2):
	if not isinstance(month1, int):
		month1 = month_number(month1)
	if not isinstance(month2, int):
		month2 = month_number(month2)
	return abs(month2 - month1)



