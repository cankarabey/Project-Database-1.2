from datetime import *
from datetime import date
import datetime

def futureDate(mydate):
    entry6_format = '%Y-%m-%d'
    datetime_obj = datetime.datetime.strptime(mydate, entry6_format)
    if datetime_obj.date() <= date.today():
        return False
    else:
        return True

print(futureDate("2022-01-01"))
