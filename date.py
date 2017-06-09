from operator import mod
from datetime import datetime
from datetime import timedelta
import sys
import pandas as pd

timestr=sys.argv[1]
#timestr='2016-02-01'
Y=int(timestr[0:4])
M=int(timestr[6:7])
D=int(timestr[8:])
cday = datetime.strptime(timestr, '%Y-%m-%d')
oneday=cday-timedelta(days=1)

print(cday.strftime('%Y-%m-%d'))
############first#########################
oneday1=cday-pd.tseries.offsets.DateOffset(days=1)
monday1=cday-pd.tseries.offsets.DateOffset(months=1)
yday1=cday-pd.tseries.offsets.DateOffset(months=12)
print(oneday1.strftime('%Y-%m-%d'))
print(monday1.strftime('%Y-%m-%d'))
print(yday1.strftime('%Y-%m-%d'))
############second########################
if (mod(Y,4)==0)or(mod(Y,400)==0):
	if M==2 and D==29:
		monday=cday-timedelta(days=31)
		yday="N"
	elif M==2:
		monday=cday-timedelta(days=31)
		yday=cday-timedelta(days=365)
	else:
		if M==3 and D>=30:
			monday="N"
		elif M==3:
			monday=cday-timedelta(days=29)
		elif M in [1,5,7,8,10,12]:
			monday=cday-timedelta(days=30)
		else:
			monday=cday-timedelta(days=31)
		yday=cday-timedelta(days=366)
else:
	if M==3 and D>=29:
		monday="N"
	elif M==3:
		monday=cday-timedelta(days=28)
	elif M in [1,5,7,8,10,12]:
		monday=cday-timedelta(days=30)
	else:
		monday=cday-timedelta(days=31)
	yday=cday-timedelta(days=365)
print(oneday.strftime('%Y-%m-%d'))
print(monday.strftime('%Y-%m-%d'))
print(yday.strftime('%Y-%m-%d'))


