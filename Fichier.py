import json
with open('Fichier.json', 'r') as file:
    Fichier = json.load(file)

def create(name, ID):
    cre = False
    crea = False
    while not cre:
        if crea:
            value = input(name + " : ")
            print(value)
            Fichier[ID][name] = value
            cre = True
        elif not name in Fichier[ID]:
            crea = True
        else:
            name = input("Veuillez modifier le nom du fichier : ")
            print(name)
    with open('Fichier.json', 'w') as file:
        json.dump(Fichier, file)

def View(ID):
    for fichier in Fichier[ID].keys():
        print(fichier)

def Open(ID):
    A = True
    while A:
        name = input('Quel fichier : ')
        if name in Fichier[ID]:
            print(Fichier[ID][name])
            A = False
        elif name == "^V":
            A = False
        else:
            print("Ce fichier n'existe pas.")

def Delete(ID):
    A = True
    while A:
        name = input('Quel Fichier : ')
        print(name)
        if name in Fichier[ID]:
            del Fichier[ID][name]
            A = False
        elif len(Fichier[ID]) == 0:
            A = False
        else:
            print("Ce fichier n'existe pas.")
    with open('Fichier.json', 'w') as file:
        json.dump(Fichier, file)

def Modify(ID):
    A = True
    while A:
        name = input('Quel Fichier : ')
        print(name)
        if name in Fichier[ID]:
            vallue = input("")
            print(vallue)
            Fichier[ID][name] = vallue
            A = False
        elif len(Fichier) == 0:
            A = False
        else:
            print("Ce fichier n'existe pas.")
    with open('Fichier.json', 'w') as file:
        json.dump(Fichier, file)
