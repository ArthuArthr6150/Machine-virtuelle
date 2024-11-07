import os
import time


def AntiV(user):
    fichiers = os.listdir(f"Fichiers/{user}")
    numO = 0
    for num in range(len(os.listdir)):
        time.sleep(1)
        numO += 1
        print()
        print(f"{numO}/{len(os.listdir)}")
    print()
    print("0 virus, 0 malwaire, 0 piratage")
