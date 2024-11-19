class Car():
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def show(self):
        print('La marca del carro es: ', self.brand, ', su modelo es: ', self.model, 'y tiene un precio de: $USD', self.price)
