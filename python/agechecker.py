import datetime

# tanya user utk memasukan tahun kelahiran
y = input('Enter your birth year: ')
# tanya user utk memasukan bulan kelahiran
m = input('Enter your birth month: ')
# tanya user utk memasukan tanggal kelahiran
d = input('Enter your birth day: ')

year = int(y)
month = int(m)
day = int(d)

birthday = datetime.date(year=year, month=month, day=day)
today = datetime.date.today()

age_delta = today - birthday
age = age_delta.days / 365

# check apakah user sudah lebih dari 17 tahun, if yes "welcome", if no "try next time"
if age >= 17:
    print("Welcome")
else:
    print("Coba lagi nanti")