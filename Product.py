class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"Product: {self.name}, Price: ${self.price}, Stock: {self.stock}"
