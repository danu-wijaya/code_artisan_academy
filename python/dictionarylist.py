countries = [
    {
        'name': 'Republik Indonesia',
        'president': 'Joko Widodo',
        'capital': 'Jakarta',
        'population': 250000000
    },
    {
        'name': 'Germany',
        'president': 'Angela Merkel',
        'capital': 'Berlin',
        'population': 67000000
    },
    {
        'name': 'USA',
        'president': 'Donald Trump',
        'capital': 'Washinton D.C',
        'population': 400000000
    },
]

for c in countries:
    print(c['name'])

# tampilkan total jumlah penduduk dari semua negara
total = 0

for c in countries:
    population = c['population']
    # total += population ... sama dengan total = total + population
    total += population

print(total)

numbers = [5,3,2]
print(sum(numbers))

