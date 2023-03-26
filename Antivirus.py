import json
import time


def AntiV():
    numO = 0
    with open('Fichier.json', 'r') as file:
        Fichier = json.load(file)
    for num in range(len(Fichier)):
        numO += 1
        print(f"{numO}/{len(Fichier)}")
        time.sleep(1)