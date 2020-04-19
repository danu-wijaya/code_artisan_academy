news = "Hari ini terjadi hujan badai kemarin juga Badai"

# hitung ada berapa kata "badai"

print(news.lower().count("badai")) 
print(len(news))
print(news[10])

# index function to find the position of a character
print(news.index("ini"))

# ceheck wether string strart with
print(news.startswith("Hari"))

# endwidth
print("email@kamandanu.id".endswith(".id"))

print("user logout".replace("logout", "keluar"))

# meng"hilangkan space depan belakang
print(" hello world   ".strip())

print("hello".isalpha())
print("12343".isnumeric())
print("123kdj".isalpha())