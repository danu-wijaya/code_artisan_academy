cities = ['jakarta', 'bandung', 'surabaya']

print(len(cities))

# add item to a list
cities.append("denpasar")

print(len(cities))
print(cities)

# akses item di dalam list menggunakan index
print(cities[1])

# add item in a specific position
cities.insert(1, "semarang")
print(cities)

# count
print(cities.count('jakarta'))
# membership
print("jakarta" in cities)

