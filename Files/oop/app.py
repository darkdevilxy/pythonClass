class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f'Hi Iam {self.name}')


person1 = Person("Dark Devil")
person1.talk()

person2 = Person("Abyss Queen")
person2.talk()
