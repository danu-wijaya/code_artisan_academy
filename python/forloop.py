fruits = ['apple', 'orange', 'durian', 'rambutan']

for f in fruits:
    print(f.upper())

for s in "hello":
    print(s)

hobbies = "soccer, coding, golf"

# print(hobbies.split(", "))

for hobby in hobbies.split(','):
    print("Your hobby is {0}".format(hobby.strip()))

# range akan menghasilkan sebuat list dari angka antara mulai sampai satu sebelum akhir
for x in range(1,10):
    print(x)

# print angka genap antara 50-70
angka_genap = []
angka_ganjil = []

for x in range(50, 71):
    if x % 2 == 0:
        angka_genap.append(x)
    else:
        angka_ganjil.append(x)

for y in angka_genap:
    print(y)