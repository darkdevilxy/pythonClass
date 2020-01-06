# AND want for all condition to return true
# OR at least one condition should return true
# NOT want the condition to return false


name = input("Enter your name: ")
a = len(name)
if a > 30:
    print(f"Your name is way too long.")
elif a < 3:
    print(f"Your name is way to short.")
else:
    print(f"Your name looks good.")

