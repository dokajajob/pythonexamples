from dateutil.relativedelta import relativedelta

myBirthday = datetime.datetime(1947,5,5,0,0,0,0)
now = datetime.datetime.now()



difference = relativedelta(now, myBirthday)
print("My years: "+str(difference.years))

