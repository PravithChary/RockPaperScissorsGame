# Rock paper scissors Game
# Rock wins over Scissors but loses on Paper
# Paper wins over Rock but loses over Scissors
# Scissors wins over Paper but loses over Rock

import random


def game(you, comp):
    if comp == you:
        return None
    elif comp == "r":
        if you == "p":
            return True
        elif you == "s":
            return False
    elif comp == "p":
        if you == "s":
            return True
        elif you == "r":
            return False
    elif comp == "s":
        if you == "r":
            return True
        elif you == "p":
            return False


randNo = random.randint(1, 3)  # chooses any int from 1 to 3
if randNo == 1:
    comp = "r"
elif randNo == 2:
    comp = "p"
else:
    comp = "s"

print("Comp Turn : rock (r), paper (p), scissors (s):  ")
you = input("Your Turn : rock (r), paper (p), scissors (s):  ")

print(f"Comp chose {comp}")
print(f"You chose {you}")

a = game(you, comp)

if a == None:
    print("Try again")
elif a:
    print("You\'ve won")
else:
    print("You\'ve lose")
