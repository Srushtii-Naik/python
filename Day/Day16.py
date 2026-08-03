'Python datetime'

#Python has got datetime module to handle date and time.
import datetime
print(dir(datetime))

#Getting datetime Information
from datetime import datetime
now = datetime.now()
print(now)
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
second = now.second
timestamp = now.timestamp()
print(day,month,year,hour,minute)
print('timestamp',timestamp)
print(f'{day} / {month} / {year} , {hour}: {minute}')


#Formatting Date Output Using strftime
from datetime import datetime
new_year = datetime(2026,8,3)
print(new_year)
day = new_year.day
month = new_year.month
year = new_year.year
hour = new_year.hour
minute = new_year.minute
second = new_year.second
print(day, month, year, hour, minute)
print(f'{day}/{month}/{year}, {hour}:{minute}') 


#Formatting date time using strftime method
'strftime() converts a date/time object into a formatted string'
from datetime import datetime
now = datetime.now()
t = now.strftime('%H:%M:%S')
print('time: ', t)


#Common Format Codes
from datetime import datetime
now = datetime.now()

print(now.strftime("%d"))   #Day
print(now.strftime("%m"))   #Day
print(now.strftime("%Y"))   #4-digit Year
print(now.strftime("%y"))   #2-digit Year
print(now.strftime("%H"))   #Hour (24-hour)
print(now.strftime("%I"))   #Hour (12-hour)
print(now.strftime("%M"))   #minutes
print(now.strftime("%S"))   #Seconds
print(now.strftime("%p"))   #Am/Pm
print(now.strftime("%A"))   #Full weekday
print(now.strftime("%a"))   #Short weekday
print(now.strftime("%B"))   #Full month
print(now.strftime("%b"))   #short month



#strptime() converts a string into a datetime object
from datetime import datetime
date = datetime.strptime("03-08-2026", "%d-%m-%Y")
print(date)

#timedelta is used to add or subtract dates
from datetime import datetime, timedelta
today = datetime.now()
future = today + timedelta(days=10) #Add Days
print(future)
past = today - timedelta(days=5)    #Subtract Days

print(past)

#Difference Between Two Dates
from datetime import date
d1 = date(2026, 8 , 3)
d2 = date(2026, 8 , 10)
diff = d2 - d1
print(diff.days)

#Compare Dates
from datetime import date
d1 = date(2026, 8 , 3)
d2 = date(2026, 8 , 10)
print(d1 < d2)

#Calendar Example
import calendar
print(calendar.month(2026,8))


# ___________________________________________________________________________________________________________________________________________________________________________________

from datetime import datetime
print(datetime.now().year)  #Get Current Year
print(datetime.now().strftime("%A"))#Get Current Weekday
print(datetime.now().strftime("%I:%M:%S:%p"))

# ___________________________________________________________________________________________________________________________________________________________________________________



# #Get the current day, month, year, hour, minute and timestamp from datetime module
from datetime import datetime
now = datetime.now()
print("Day: ",now.day)
print("Month: ",now.month)
print("Year: ",now.year)
print("hour: ",now.hour)
print("Minute: ",now.minute)
print("Timestamp: ",now.timestamp())

#Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
formatted = now.strftime("%d/%m/%y, %H:%M:%S")
print(formatted)

#Today is 3 August, 2026. Change this time string to time.
date_string = "3 August, 2026"
converted = datetime.strptime(date_string, "%d %B, %Y")
print(converted)

#Calculate the time difference between now and new year
new_year = datetime(year=now.year + 1, month=1, day=1)
diff = new_year - now
print(diff)

#Calculate the time difference between 1 January 1970 and now.
epoch = datetime(1970, 1, 1)
diff_epoch = now - epoch
print("Time since 1970:", diff_epoch)