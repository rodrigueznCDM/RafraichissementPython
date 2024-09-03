import random
def addition():

    numero1 = int(input("entrez votre premier numéro (entier):\n"))
    numero2 = int(input("entrez votre deuxième numéro (entier):\n"))
    somme = numero1 + numero2
    print("le résultat de",numero1,"additioné à",numero2,"est de",somme)

def division():

    numero1 = int(input("entrez votre premier numéro (entier et pas zero):\n"))
    if numero1 == 0:
        print("entrez un numéro autre que zero la prochaine fois")
        exit("-1")

    numero2 = int(input("entrez votre deuxième numéro (entier):\n"))
    if numero2 == 0:
        print("entrez un numéro autre que zero la prochaine fois")
        exit("-1")

    produit = numero1 / numero2
    print("le résultat de",numero1,"divisé par",numero2,"est de",produit)

def PairOuImpair(num1, num2):
    pair = 0
    impair = 0
    num2 = num2 + 1
    for i in range(num1, num2):
        typeCheck = i % 2
        if typeCheck == 0:
            pair = pair + 1
            print(i, "est pair")

        else:
            impair = impair + 1
            print(i, "est impair")

    print("il y a", pair, "chiffre(s) pair(s) et", impair, "chiffre(s) impair(s) dans cette séquance")
    exit()

def d6():
    resultat = random.randint(1,6)
    return resultat


exercices = input("quel exercice voulez vous regarder?:\n")

if exercices == "1":
    print("\nNOM\n")
    nom = input("quel est votre nom?:\n")
    print("Bonjour",nom,"Comment allez vous?")
    exit()

elif exercices == "2":
    print("\nADDITION\n")
    addition()
    exit()

elif exercices == "3":
    print("\nDIVISION\n")
    division()
    exit()

elif exercices == "4":
    print("\nPAIR OU IMPAIR\n")
    pair = 0
    impair = 0
    for i in range(1,10):
        typeCheck = i % 2
        if typeCheck == 0:
            pair = pair + 1
            print(i,"est pair")

        else:
            impair = impair + 1
            print(i,"est impair")

    print("il y a",pair,"chiffre(s) pair(s) et",impair,"chiffre(s) impair(s) dans cette séquance")
    exit()

elif exercices == "5":
    print("\nPAIR OU IMPAIR CHOISIR\n")
    num1 = int(input("entrez le premier numéro de la séquance voulue (entier):\n"))
    num2 = int(input("entrez le deuxième numéro de la séquance voulue (entier):\n"))
    PairOuImpair(num1, num2)
    exit()

elif exercices == "6":
    print("\nDÉ À SIX FACES\n")
    print("on lance le dé...")
    resultat = d6()
    print("le dé est tombé sur",resultat)
    exit()

elif exercices == "7":
    print("")

else:
    exit()