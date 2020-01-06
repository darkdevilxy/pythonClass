name = input("Name: ")
age = input("Age: ")
weight = input("Kindly enter your weight: ")
print("Hello " + name)
lbs = 2.5 * float(weight)
print(name.replace(name, f'{name} .jr'))
print("Hello so you are {}". format(lbs) + " lbs")
if int(age) < 18:
    print("You are underage by {}" .format(18 - int(age)) + " years")
else:
    print("Welcome abroad")
