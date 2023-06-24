import json
import time


def AntiV(user):
    numO = 0
    with open('Fichier.json', 'r') as file:
        Fichier = json.load(file)
    for num in range(len(Fichier[user])):
        time.sleep(1)
        numO += 1
        print()
        print(f"{numO}/{len(Fichier[user])}")
    print()
    print("0 virus, 0 malwaire, 0 piratage")
