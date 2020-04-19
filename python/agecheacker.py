import datetime

# year = int(input("masukan tahun lahir : "))
# month = int(input("masukan bulan lahir : "))
# day = int(input("masukan tanggal lahir : "))

# birthday = datetime.date(year=year, month=month, day=day)
# today = datetime.date.today()

# age_delta = today - birthday
# age = age_delta.days / 365

# if age >= 17:
#     print("welcome")
# else:
#     print("coba lagi nanti")

print(today.strftime('%B %d, %Y'))
