# integer is number / angka
x = 2
y = 3

# math operation +, -, *, /, %
print("x + y = {result}".format(result=x + y))
print("x * y = {result}".format(result=x * y))
print("x - y = {result}".format(result=x - y))
# round() utk membulatkan angka round(0.781212121, 2) -> 0.78
print("x / y = {result}".format(result=round(x / y,2)))

z = 5
y = 3

print(z/y)
# % modulo memberikan sisa pembagian
print(z%y)

score = 30
level = 10

if score % level == 0:
    print("naik level")
else:
    print("get more score")