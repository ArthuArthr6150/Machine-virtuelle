
def Paral():
    while True:
        try:
            Num1 = int(input('Votre base : '))
            break
        except ValueError:
            print('Ce doit être un nombre entier.')
    while True:
        try:
            Num2 = int(input('Votre hauteur : '))
            break
        except ValueError:
            print('Ce doit être un nombre entier.')

    print('Votre aire : ' + str(Num1 * Num2))