import random

def Alléatoire():
    A = True
    def Min():
        while A:
            try:
                min = int(input("Donnez-moi votre nombre minimal : "))
                print(str(min))
                break
            except ValueError:
                print("Veillez à garder un nombre entier.")
        Max(min)

    def Max(min):
        while True:
            try:
                max = int(input("Donnez-moi votre nombre maximal : "))
                if max <= min:
                    raise ValueError("Il doit être entier et plus grand que le minimum.")
                print(str(max))
                break
            except ValueError as e:
                print(e)
        final(min, max)

    def final(min, max):
        print("Min = " + str(min))
        print("Max = " + str(max))
        print(random.randint(min, max))
        A = False

    Min()