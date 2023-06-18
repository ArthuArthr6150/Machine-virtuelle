from getpass import getpass
import json
import random
import hashlib

with open("Fichier.json", "r") as file:
    fichiers = json.load(file)
with open("Code.json", "r") as file:
    codes = json.load(file)

def Parametre(code, users, username, user):
    print("""Les paramêtre : 
Changer le mot de passe
Créer un nouvel utilisateur
Changer d'utilisateur
Détruire un utilisateur""")
    print()
    pch = input("""Quel paramêtre(à écrire tel quel)?
""")
    print()
    if pch == "Changer le mot de passe":
        cod = getpass("Votre code pour continer : ")
        sha = hashlib.sha256()
        cod_byte = cod.encode('utf-8')
        sha.update(cod_byte)
        cod_hache = sha.hexdigest()
        if cod_hache == code :
            nCode = getpass("Votre nouveau code : ")
            vCode = getpass("Votre code à nouveau : ")
            if nCode == vCode:
                sha = hashlib.sha256()
                ncode_byte = nCode.encode('utf-8')
                sha.update(ncode_byte)
                ncode_hache = sha.hexdigest()
                codes[users[nuser]] = ncode_hache
                with open("Code.json", "w") as file:
                    json.dump(nCode, file)
        else: print("Ce n'est pas le bon code")
    elif pch == "Créer un nouvel utilisateur":
        nuser = input("Comment voulez-vous vous appeler : ")
        users[nuser] = random.randint(0, 10000)
        fichiers[users[nuser]] = {}
        print()
        code = getpass("Quel est votre code : ")
        codes[users[nuser]] = code
        with open("Fichier.json", "w") as file:
            json.dump(fichiers, file)
        with open("Code.json", "w") as file:
            json.dump(codes, file)
        with open("Users.json", "w") as file:
            json.dump(users, file)
    elif pch == "Changer d'utilisateur":
        print("Voisi les utilisateur enregistré:")
        for i in users:
            print(i)
        while True:
            print()
            usersel = input("Quel utilisateur : ")
            if usersel in users:
                usernames = usersel
                return usernames
            else: print("Cet utilisateur n'est pas connu.")
    elif pch == "Détruire un utilisateur":
        print("Voisi les utilisateur enregistré:")
        for i in users:
            print(i)
        while True:
            print()
            usersel = input("Quel utilisateur : ")
            if usersel in users:
                del users[usersel]
                del fichiers[user]
                del code[user]
                with open("Users.json", "r") as file:
                    users = json.load(file)
                if len(users) == 0 or usersel == username:
                    return True
                else: break
            else: print("Cet utilisateur n'est pas connu.")
    else: print("Ce paramêtre n'est pas connu/n'existe pas. Vous pouvez vérifier la version de votre MV.")
