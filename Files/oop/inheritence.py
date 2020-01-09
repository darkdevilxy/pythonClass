from data_1 import  Point
from app import Person

class Mammal:
    def walk(self):
        print("Hello World")


class Dog(Mammal):
    pass


class Cat(Mammal):
    pass


dog1 = Point(1, 2)
dog1.move()

john = Person("John")
john.talk()

