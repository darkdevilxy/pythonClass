import math
turn = 0
while turn < 3:
    guess = input(f"Guess: ")
    a = int(guess)
    if a == 9:
        print(f"You win")
        break
    elif a != 9:
        turn += 1
    print(f'You Lose')


