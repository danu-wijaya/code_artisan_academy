# ini sebuah object tipe text atau String
print("This is a text or String")

print(len("Hello"))

# variable with a type of string / variable dengan tipe string
first_name = 'Arifin' # literal
last_name = 'doe'

print(first_name.upper())

# string concatination / join / menggabungkan
print(first_name.title() + " " + last_name.title()) 

# Hello mr John Doe, apa kabar
# using label for the place holder
print("Hello mr {f_name} {l_name}, apa kabar".format(f_name=first_name.title(), l_name=last_name.title()))
# using index for the place holder
print("Hello mr {0} {1}, apa kabar".format(first_name.title(), last_name.upper()))

greeting = "Mr."

# Hi Mr. John Doe, How are you?
print("Hi {greeting} {f_name} {l_name}, How are you?".format(greeting=greeting, f_name=first_name, l_name=last_name))

# Hello John, your name has 4 letters
print("Hello {name}, your name has {total} letters".format(name=first_name, total=len(first_name)))

