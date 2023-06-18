from getpass import getpass
import hashlib

def Verrouillage(code_hash):
    dév = False
    while not dév:
        ask = getpass("Donne moi le mot de passe : ")
        sha = hashlib.sha256()
        ask_byte = ask.encode('utf-8')
        sha.update(ask_byte)
        ask_hache = sha.hexdigest()
        if ask_hache != code_hash:
            print("Mot de passe incorecte.")
        else:  
            dév = True
    return dév
        
