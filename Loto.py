import random

def loto():
    correct = 0
    Mynumbers = []
    numbers = [random.randint(1,9),random.randint(1,9),random.randint(1,9),random.randint(1,9),random.randint(1,9)]
    while True:
        try:
            for a in numbers:
                Mynumber = int(input("Votre nombre : "))
                print(Mynumber)
                if Mynumber > 9 or Mynumber < 1:
                    raise ValueError("Ce doit être un nombre qui doit être entier et compris entre 1 et 9 inclus.")
                Mynumbers.append(Mynumber)
            break
        except ValueError as e:
            print(e)
            Mynumbers = []
    for Nombre in range(len(numbers)):
        if numbers[Nombre] == Mynumbers[Nombre]:
            correct += 1
    if correct == 5:
        print("Vous avez gagné.")
    elif correct == 0:
        print("Vous êtes un looser.")
    else:
        print(f"Vous avez eu {correct} nombre correcte.")
