countries = [
    {
    'name': 'indonesia',
    'presiden': 'jokowi',
    'capital': 'jakarta',
    'population': 250000000
    },
    {
    'name': 'germany',
    'presiden': 'angela markel',
    'capital': 'berlin',
    'population': 67000000
    },
    {
    'name': 'usa',
    'presiden': 'trump',
    'capital': 'washington',
    'population': 400000000
    },
]

# total = []
# for c in countries:
#     total.append(c['population'])
    
# print(sum(total))
total = 0
for c in countries:
    population = c['population']
    total += population
print(total)

