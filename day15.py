

#------------------> PYTHON DATE AND TIME <--------------------


# datetime : it has got from datetime module to handel date and time

import datetime
print(dir(datetime))

# o/p:['MAXYEAR', 'MINYEAR', 'UTC', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', 
#      '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'time', 'timedelta', 'timezone', 'tzinfo']



# getting date time information

from datetime import datetime
now_time=datetime.now()
print(now_time)# its show time according to our system,if system time is wrong it also shows wrong  time

day_date=now_time.day
print(day_date)

month=now_time.month
print(month)

this_year=now_time.year
print(this_year)

now_hour=now_time.hour
print(now_hour)

now_minute=now_time.minute
print(now_minute)

now_second=now_time.second
print(now_second)

time_stamp=now_time.timestamp()
print(time_stamp)

#  formatingvdata output using strftime

from datetime import datetime
new_year=datetime(2025,5,26,12,22,49)
print(new_year)

day_date=new_year.day
print(day_date)

month=new_year.month
print(month)

this_year=new_year.year
print(this_year)

now_hour=new_year.hour
print(now_hour)

now_minute=new_year.minute
print(now_minute)

now_second=new_year.second
print(now_second)

time_stamp=new_year.timestamp()
print(time_stamp)

#    |
#    |
#    |
#    v
from datetime import datetime
now=datetime.now()
t=now.strftime("%H:%M:%S")
print(t)

time_one=now.strftime("%d/%m/%Y,%H:%M:%S")
print(time_one)

# %a  sun
# %A  sunday
# %w  sunday as number 1
# %W  week number of year,monday 2nd day of week,so in whole year it is total 52 because each week 4 monday,0-53
# %d  day of month 1-31
# %b  month in sort, Dec.
# %B  month in full, December
# %m  month as number 1-12
# %M  minute 0-59
# %y  year sort version , 25
# %Y  year full version , 2025
# %H  hour 00-23
# %I  hour 00-12
# %p  AM/PM
# %S  second 00-59  
# %f  micro second , 000000-999999
# %z  UTC offset
# %Z  timezone
# %j  day number of year ,001-366
# %U  week number of year,sunday 1st day of week,so in whole year it is total 52 because each week 4 sunday,0-53
# %c  local version of date and time
# %x  local version of date
# %X  local version of time
# %%  A% character


# string to time using:- strptime()

from datetime import datetime
date_string="5 December  ,2025"# if we use space then date time formating also use same space otherwise we get error,here 2 spce after dec
print(date_string)
date_obj=datetime.strptime(date_string,"%d %B  ,%Y")# we have to give 2 sapce after %B, to match with correct form of string
print(date_obj)

# using date from date time

from datetime import date
d=date(2025,5,26)
print(d)
print(d.today())
today=date.today()
print(f"{today.year}/{today.month}/{today.day}")

# time object to represent time: time(hour,min,sec)

from datetime import time
a=time()# time(0,0,0)
print(a)

b=time(10,30,50)
print(b)

c=time(hour=10,minute=30,second=50)
print(c)

d=time(10,30,50,200555)
print(d)

# difference between 2 point in time using

from datetime import date
today=date(year=2025,month=5,day=26)
new_year=date(year=2026,month=1,day=1)
time_left_for_new_year=new_year-today
print(time_left_for_new_year)

# difference between 2 point in time using : timedelta module

from datetime import timedelta
t1=timedelta(weeks=12,days=10,hours=4,seconds=20)
t2=timedelta(days=7,hours=5,minutes=3,seconds=30)
t3=t1-t2
print(t3)