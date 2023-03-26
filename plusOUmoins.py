import random

def PlusOuMoins():
    number = random.randint(1, 1000)
    life = 10
    while True:
        try:
            MyNum = int(input('Votre nombre : '))
            if life > 0:
                life -= 1
                if MyNum > number:
                    raise ValueError('Moins')
                elif MyNum < number:
                    raise ValueError('Plus')
                elif MyNum != number:
                    raise ValueError('Ce doit être un nombre entier positif.')
            print(f"Tu n'as plus que {life} vies.")
            break
        except ValueError as e:
            print(e)
    if life > 0:
        print('Great Job')
    else:
        print("Tu n'as plus de vies. You are a LOOSER.")