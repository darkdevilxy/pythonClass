weight = input(f"Kindly enter your weight: ")
unit = input(f"(L)bs or (K)g ")
unit.lower()
if unit == "l":
    print(f"Your weight in kilograms is {int(weight) * 0.75}")
else:
    print(f"Your weight in lbs is {int(weight) * 2.5}")

