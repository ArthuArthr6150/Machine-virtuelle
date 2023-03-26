from getpass import getpass

def Verrouillage(code):
    dév = False
    while not dév:
        ask = getpass("Donne moi le mot de passe : ")
        if ask != code:
            print("Mot de passe incorecte.")
        else:  
            dév = True
    return dév
        