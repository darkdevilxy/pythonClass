dictionary = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    "0": "zero",
}
number = input("Enter any number you like: ")
b = 0
c = ""
for x in range(len(number)):
    a = f"{dictionary.get(number[b])} "
    c += a
    b += 1
print(c)
