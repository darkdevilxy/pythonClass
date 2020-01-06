price = 1000000
credit = input("Enter the amount that you can offer: ")
if int(credit) > 2 * price:
    print(f"The final price of the house is {price - 10/100 * price} ")
else:
    print(f"The final  price of the house is {price - 20/100 * price}")
