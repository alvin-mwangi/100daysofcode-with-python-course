Python 3.7.1 (default, Dec 10 2018, 22:54:23) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from datetime import datetime
>>> from datetime import date
>>> 
>>> 
>>> datetime.today()
datetime.datetime(2019, 3, 25, 10, 6, 45, 224478)
>>> 
>>> today = datetime.today()
>>> 
>>> type(today)
<class 'datetime.datetime'>
>>> 
>>> todaydate = date.today()
>>> 
>>> type(todaydate)
<class 'datetime.date'>
>>> 
>>> todaydate
datetime.date(2019, 3, 25)
>>> 
>>> 
>>> 
>>> 
>>> 
>>> todaydate.month
3
>>> type(todaydate.month)
<class 'int'>
>>> todaydate.day
25
>>> todaydate.year
2019
>>> today.minute
7
>>> 
>>> 
>>> 
>>> christmas = date(2019, 12, 25)
>>> type(christmas)
<class 'datetime.date'>
>>> christmas
datetime.date(2019, 12, 25)
>>> 
>>> 
>>> christmas - todaydate
datetime.timedelta(days=275)
>>> 
>>> (christmas - todaydate).days
275
>>> 
>>> if christmas is not todaydate:
	print("Sorry, there are still " + str((christmas - todaydate).days) + " days until Christmas!")
else:
	print("Yay it's Christmas!")

	
Sorry, there are still 275 days until Christmas!
>>> 
