from Aléaroire import Alléatoire
from Déverouille import Verrouillage
from Fichier import create
from Fichier import View
from Fichier import Open
from Fichier import Delete
from Fichier import Modify
from Jeu.plusOUmoins import PlusOuMoins
from Jeu.Loto import loto
from Antivirus import AntiV
from Para import Paral
from Paramêtre import Parametre
from Calculator import Calcul
import json
import random
from getpass import getpass
import hashlib

print("<!> On ne supporte pas windows. <!>")
print("""Pour connaitre les commandes il y a la commande Help.
""")

username = ""
user = ""
with open("Users.json", "r") as file:
    users = json.load(file)
if len(users) > 0:
    print("Voisi les utilisateur enregistré:")
    for i in users:
        print(i)
    while True:
        print()
        usersel = input("Quel utilisateur : ")
        if usersel in users:
            user += str(users[usersel])
            username += usersel
            break
        else: print("Cet utilisateur n'est pas connu.")
else:
    with open("Fichier.json", "r") as file:
        fichiers = json.load(file)
    with open("Code.json", "r") as file:
        codes = json.load(file)
    nuser = input("Comment voulez-vous vous appeler : ")
    users[nuser] = random.randint(0, 10000)
    fichiers[users[nuser]] = {}
    username += nuser
    print()
    code = getpass("Quel est votre code : ")
    with open("Fichier.json", "w") as file:
        json.dump(fichiers, file)
    sha = hashlib.sha256()
    code_byte = code.encode('utf-8')
    sha.update(code_byte)
    code_hache = sha.hexdigest()
    codes[users[nuser]] = code_hache
    with open("Code.json", "w") as file:
        json.dump(codes, file)
    with open("Users.json", "w") as file:
        json.dump(users, file)
    user += str(users[nuser])

print(f"""
Bienvenue {username}.      
""")
with open("Code.json", "r") as file:
    codes = json.load(file)
code = codes[user]
run = True
dév = False
play = False

while run:
    
    if dév == False:
        com = input("Python> ")
    elif dév == True and play == False:
        com = input("Python/User> ")
    else:
        com = input("Python/User/Vidéo_Games> ")
    print()
    
    
    if dév == True:
        if play == True:
            if com == "cd /":
                play = False
            elif com == 'Help':
                CommandesP = {"cd /":"Retour à la gestion des fichier.","PlusOuMoins":"Jeu où tu dois deviner un nombre entre 0 et 1000","Lotto":""}
                print(CommandesP)
            elif com == 'PlusOuMoins':
                PlusOuMoins()
            elif com == 'Lotto':
                loto()
        elif com == 'Help' and play == False:
            Commandes = {"Calculatrice":"Petite calculatrice digne de la 'Petite FX'",'Paramêtre':'Permet de changer des paramêtres.','AntiVirus':'Bloque les virus.',"Play":"Permet d'accèder aux jeux vidéo.","Off":"Eteins la MV.","Modify":"Modifier un fichier.","Delete":"Suprime un fichier.","Open":'Ouvre le fichier de notre choix','Create':"Créer des fichier","Help":"Connaitre les fonction","Aléatoire":"Donner un nombre aléatoire entre un minimum et un maximum","Déverrouille":"Donne acces à d'autre commandes","View":"Permet de voir les fichier existant."}
            print(Commandes)
        elif com == "Create":
            com = input("Le nom : ")
            print(com)
            create(com, user)
        elif com == "View":
            View(user)
        elif com == "Open":
            Open(user)
        elif com == "Delete":
            Delete(user)
        elif com == "Modify":
            Modify(user)
        elif com == "Aléatoire":
            Alléatoire()
        elif com == "Play":
            play = True
        elif com == "AntiVirus":
            AntiV()
        elif com == "Paramêtre":
            c = Parametre(code, users, username, user)
            if c in users:
                username = c
                user = users[c]
            elif c == True:
                print(f"A dieu, utilisateur {username}")
                run = False
            with open("Users.json", "w") as file:
                json.dump(users, file)
            with open("Fichier.json", "r") as file:
                fichiers = json.load(file)
            with open("Code.json", "r") as file:
                codes = json.load(file)
        elif com == "Calculatrice":
            Calcul()
        elif com == "Off":
            print(f"Au revoir {username}")
            run = False
        elif com == "Paral":
            Paral()
        else: print("Cette commande n'est pas connue/n'existe pas. Vous pouvez vérifier la version de votre MV.")
    elif com == "Help" and dév == False:
        CommandesV = {"Off":"Eteins la MV.","Help":"Connaitre les fonction","Aléatoire":"Donner un nombre aléatoire entre un minimum et un maximum","Déverrouille":"Donne acces à d'autre commandes"}
        print(CommandesV)
    elif com == "Déverrouille":
        if Verrouillage(code):
            dév = True
    elif com == "Off":
        print(f"Au revoir {username}")
        run = False
    elif com == "Paral":
        Paral()
    else: print("Cette commande n'est pas connue/n'existe pas. Vous pouvez vérifier la version de votre MV.")
    print()
