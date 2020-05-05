class Auto:

    def __init__(self, model, wheels):
        self._fuel = 'Gas'
        self._model = model
        self._wheels = wheels

    def __str__(self):
        return ' Class Auto '


class Car(Auto):

    def __str__(self):
        return '\n   _____ \n __/[][] |\n -0-----0-'


class Truck(Auto):

    def __str__(self):
        return '\n    _____     \n __/[][] |____\n -0-------0-0-'


a = Auto('BMW', 4)
b = Car('Mercedess', 4)
c = Truck('MAN', 6)

print(a, b, c)

