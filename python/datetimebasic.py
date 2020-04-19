import datetime

"""
today = datetime.date.today()
days = ['senin', 'selasa', 'rabu', 'kamis', 'jumat', 'sabtu', 'minggu']
print(today)

print("The year is {0}".format(today.year))
print("The year is {0}".format(today.month))
print("The year is {0}".format(today.day))

weekday = today.weekday()
print("hari ini. hari {0}".format(days[weekday]))

now = datetime.datetime.now()

print(now.hour)

proklamasi = datetime.date(year=1945, month=8, day=17)
print(proklamasi)

from_proklamasi = today - proklamasi

print(from_proklamasi.total_second())

"""
today = datetime.date.today()
# April 15, 2020 %B %d, %Y
print(today.strftime('%B %d, %Y'))

# APR 