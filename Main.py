from Aléaroire import Alléatoire
from Déverouille import Verrouillage
from Fichier import create
from Fichier import View
from Fichier import Open
from Fichier import Delete
from Fichier import Modify
from plusOUmoins import PlusOuMoins
from Loto import loto
from Antivirus import AntiV
from Para import Paral

code = "1234"
run = True
dév = False
play = False

print("<!> On ne supporte pas windows. <!>")
print("Pour connaitre les commandes il y a la commande Help")

while run:
    
    if dév == False:
        com = input("Python> ")
    elif dév == True and play == False:
        com = input("Python/User> ")
    else:
        com = input("Python/User/Vidéo_Games> ")
    
    
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
            Commandes = {'AntiVirus':'Bloque les virus.',"Play":"Permet d'accèder aux jeux vidéo.","Off":"Eteins la MV.","Modify":"Modifier un fichier.","Delete":"Suprime un fichier.","Open":'Ouvre le fichier de notre choix','Create':"Créer des fichier","Help":"Connaitre les fonction","Aléatoire":"Donner un nombre aléatoire entre un minimum et un maximum","Déverrouille":"Donne acces à d'autre commandes","View":"Permet de voir les fichier existant."}
            print(Commandes)
        elif com == "Create":
            com = input("Le nom : ")
            print(com)
            create(com)
        elif com == "View":
            View()
        elif com == "Open":
            Open()
        elif com == "Delete":
            Delete()
        elif com == "Modify":
            Modify()
        elif com == "Aléatoire":
            Alléatoire()
        elif com == "Play":
            play = True
        elif com == "AntiVirus":
            AntiV()
    if com == "Help" and dév == False:
        CommandesV = {"Off":"Eteins la MV.","Help":"Connaitre les fonction","Aléatoire":"Donner un nombre aléatoire entre un minimum et un maximum","Déverrouille":"Donne acces à d'autre commandes"}
        print(CommandesV)
    elif com == "Déverrouille":
        if Verrouillage(code):
            dév = True
    elif com == "Off":
        run = False
    elif com == "Paral":
        Paral()
