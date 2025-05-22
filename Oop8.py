# Inheritance = when one class(childdrived) drives the properties and methods of another class(parent/class)

class Car:
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped.")

class ToyotaCar(Car):
    def __init__(self, brand):
        self.brand = brand

class Fortuner(ToyotaCar):
    def __init__(self, type):
        self.type = type

car1= Fortuner("disel")
car1.start()
