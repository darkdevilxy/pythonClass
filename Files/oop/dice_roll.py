import random



class Dice:
    def roll(self):
        rolls = (random.randint(1, 6), random.randint(1, 6))
        return rolls


roll1 = Dice()
boom = roll1.roll()
print(boom)