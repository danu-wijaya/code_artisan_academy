class Product:
    def __init__(self, price, name, description):
        self.price = price
        self.name = print
        self.description = description
    
    def __str__(self):
        return self.name

class Computer(Product):
    def __init__(self, price, name, ram, disk, os):
        super().__init__(price=price, name=name, description=description)

class Shoe(Product):
    def __init__(self, price, name, ram, disk, os):
        pass