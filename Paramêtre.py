from getpass import getpass
import json

def Parametre(code):
    print("""Les paramêtre : 
Changer le mot de passe""")
    pch = input("""Quel paramêtre(à écrire tel quel)?
""")
    if pch == "Changer le mot de passe":
        cod = getpass("Votre ancien code pour vous vérifier : ")
        if cod == code :
            nCode = getpass("Votre nouveau code : ")
            vCode = getpass("Votre code à nouveau : ")
            if nCode == vCode:
                with open("Code.json", "w") as file:
                    json.dump(nCode, file)
    else: print("Ce paramêtre n'est pas connu/n'existe pas. Vous pouvez vérifier la version de votre MV.")
