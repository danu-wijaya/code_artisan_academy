news = "Hari ini terjadi hujan badai seperti kemarin juga badai"

# hitung ada berapa kata "badai"
# count is case sensitive
print(news.count("badai"))

print(len(news))

# index is the position of something start at 0
print(news[10])
print(news[1:10])
print(news[-4])


# index function to find the position of a character
print(news.index("ini"))

# find function to find the position of a character
print(news.find("salju"))

# startwith check apakah string dimulai dengan ... 
print(news.startswith("Hari"))

# endwith
print("wahyudi@gmai.id".endswith(".id"))

print("User logout".replace("logout","keluar"))

# menghilangkan space di depan dan belakang
print("    Hello world    ".strip())

# alphabet / huruf
print("Hello".isalpha())
print("12313".isnumeric())
print("121abc".isalnum())

# True or False -> Boolean
