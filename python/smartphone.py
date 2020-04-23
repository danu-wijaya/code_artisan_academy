class SmartPhone:
    def __init__(self, nama, os, price, color, brand, stock):
        self.nama = nama
        self.os = os
        self.price = price
        self.color = color
        self.brand = brand
        self.stock = stock
    
    def __str__(self):
        return self.brand + " " + self.nama
    
    def discount(self, discount):
        final_price = self.price - (self.price * (discount/100))
        return final_price


a50s = SmartPhone(nama="a50s", os="android", color="blue", price=2000000, brand="samsung", stock=20)
redmi8 = SmartPhone(nama="redmi8", os="android", color="red", price=1500000, brand="xiaomi", stock=5)

print(a50s.nama)
print(redmi8.nama)

print("normal price {0}".format(a50s.price))
print("discount price = {0}".format(a50s.discount(50)))