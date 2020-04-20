import datetime

today = datetime.date.today()
days = ['senin', 'selasa', 'rabu', 'kamis', 'jumat', 'sabtu', 'minggu']
print(today)

print("The year is {0}".format(today.year))
print("The year is {0}".format(today.month))
print("The year is {0}".format(today.day))

weekday = today.weekday()
print("Hari ini, hari {0}".format(days[weekday]))

now = datetime.datetime.now()

print(now.hour)

proklamasi = datetime.date(year=1945, month=8, day=17)
print(proklamasi)

# type timedelta = perbedaan antara dua waktu
from_proklamasi = today - proklamasi

print(from_proklamasi.total_seconds())

# April 15, 2020 %B %d, %Y
print(today.strftime('%B %d, %Y'))

# Apr. 15, 2020
print(today.strftime('%b %d, %Y'))

# Wednesday 15, 2020
print(today.strftime('%A %d, %Y'))

# 2020/04/15
print(today.strftime('%Y-%m-%d'))

# time delta
one_week = datetime.timedelta(weeks=1)
three_days = datetime.timedelta(days=3)

print(today + one_week)
print(today - three_days)

birthday_input = input("enter your birthday format yyyy/mm/dd: ")

birthday = datetime.datetime.strptime(birthday_input, '%Y/%m/%d')

print(birthday)