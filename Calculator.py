

def Calcul():
    opé = input("""Quelles opération entre Addition(à écrire tel quel), Soustraction(à écrire tel quel), Multiplication(à écrire tel quel),
Division(à écrire tel quel)?
""")
    while True:
        try:
            num1 = int(input("Le premier nombre : "))
            print()
            while True:
                try:
                    num2 = int(input("Le deuxième nombre : "))
                    print()
                    break
                except ValueError as e:
                    print("Il faut que se soit un nombre entier.")
            break
        except ValueError as e:
            print("Il faut que se soit un nombre entier.")
    print()
    if opé == "Addition":
        print(f"La réponse : {num1 + num2}")
    elif opé == "Soustraction":
        print(f"La réponse : {num1 - num2}")
    elif opé == "Multiplication":
        print(f"La réponse : {num1 * num2}")
    elif opé == "Division":
        if num2 == 0:
            print("On ne peut pas avoir le dividende à zéro.")
        else: print(f"La réponse : {num1 / num2}")
    else:
        print("Ce n'est pas une solution possible.")
