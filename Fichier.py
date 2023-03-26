import json
with open('Fichier.json', 'r') as file:
    Fichier = json.load(file)

def create(name):
    cre = False
    crea = False
    while not cre:
        if crea:
            value = input(name + " : ")
            print(value)
            Fichier[name] = value
            cre = True
        elif not name in Fichier:
            crea = True
        else:
            name = input("Veuillez modifier le nom du fichier : ")
            print(name)
    with open('Fichier.json', 'w') as file:
        json.dump(Fichier, file)

def View():
    for fichier in Fichier.keys():
        print(fichier)

def Open():
    A = True
    while A:
        name = input('Quel fichier : ')
        if name in Fichier:
            print(Fichier[name])
            A = False
        elif name == "^V":
            A = False
        else:
            print("Ce fichier n'existe pas.")

def Delete():
    A = True
    while A:
        name = input('Quel Fichier : ')
        print(name)
        if name in Fichier:
            del Fichier[name]
            A = False
        elif len(Fichier) == 0:
            A = False
        else:
            print("Ce fichier n'existe pas.")
    with open('Fichier.json', 'w') as file:
        json.dump(Fichier, file)

def Modify():
    A = True
    while A:
        name = input('Quel Fichier : ')
        print(name)
        if name in Fichier:
            vallue = input("")
            print(vallue)
            Fichier[name] = vallue
            A = False
        elif len(Fichier) == 0:
            A = False
        else:
            print("Ce fichier n'existe pas.")
    with open('Fichier.json', 'w') as file:
        json.dump(Fichier, file)