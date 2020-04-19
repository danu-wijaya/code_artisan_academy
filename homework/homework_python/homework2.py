countries = ['indonesia', 'singapore', 'germany']

user_country = input("Please input country : ")

if user_country in countries:
    print ('country already in the list !') 
else:
    countries.append(user_country)

print(countries)


