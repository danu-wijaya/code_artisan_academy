indonesia = {
    'name': 'indonesia',
    'presiden': 'jokowi',
    'capital': 'jakarta',
    'population': 25000000
}

print(indonesia['capital'])

indonesia['capital'] = 'kutai kartanegara'
print(indonesia['capital'])

indonesia['language'] = 'bahasa indonesia'
print(indonesia['language'])

for k in indonesia.keys():
    print(k)

for v in indonesia.values():
    print(v)

for k in indonesia.keys():
    print("the {0} is {1}".format(k, indonesia[k]))

for k, v in indonesia.items():
    print("the {0} is {1}".format(k, v))