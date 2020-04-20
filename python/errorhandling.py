import datetime

birthday_input = input("enter your birthday format yyyy/mm/dd: ")

birthday = None

try:
    birthday = datetime.datetime.strptime(birthday_input, '%Y/%m/%d')
except Exception as error:
    print("There is an error")
    print(error)
finally:
    print("Thank you")

print(birthday)