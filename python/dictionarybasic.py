indonesia = {
    'name': 'Republik Indonesia',
    'president': 'Joko Widodo',
    'capital': 'Jakarta',
    'population': 250000000
}

# print(indonesia['capital'])

indonesia['capital'] = 'Kutai Kartanegara'

print(indonesia['capital'])

indonesia['language'] = 'Bahasa Indonesia'

print(indonesia['language'])

for k in indonesia.keys():
    print(k)

for v in indonesia.values():
    print(v)

# the name is Republik Indonesia
# the president is Joko Widodo
for k in indonesia.keys():
    print("the {0} is {1}".format(k, indonesia[k]))

for k, v in indonesia.items():
    print("the {0} is {1}".format(k, v))