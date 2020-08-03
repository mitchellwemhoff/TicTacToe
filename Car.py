class Car:

    wheels = 4
    brand = 'Chevrolet'
    amount_of_gas = 5

    def __init__(self, wheels, brand):
        self.wheels = wheels
        self.brand = brand

    def add_gas(self, volume):
        self.amount_of_gas += volume
