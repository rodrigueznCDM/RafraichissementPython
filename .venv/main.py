def addition():

    numero1 = int(input("entrez votre premier numéro (entier):\n"))
    numero2 = int(input("entrez votre deuxieme numéro (entier):\n"))
    somme = numero1 + numero2
    print("le résultat de",numero1,"additioné à",numero2,"est de",somme)

def division():

    numero1 = int(input("entrez votre premier numéro (entier et pas zero):\n"))
    if numero1 == 0:
        print("entrez un numéro autre que zero la prochaine fois")
        exit("-1")

    numero2 = int(input("entrez votre deuxieme numéro (entier):\n"))
    if numero2 == 0:
        print("entrez un numéro autre que zero la prochaine fois")
        exit("-1")

    produit = numero1 // numero2
    print("le résultat de",numero1,"divisé par",numero2,"est de",produit)

exercices = input("quel exercice voulez vous regarder?:\n")

if exercices == "1":
    print("NOM\n")
    nom = input("quel est votre nom?:\n")
    print("Bonjour",nom,"Comment allez vous?")
    exit()

elif exercices == "2":
    print("ADDITION\n")
    addition()
    exit()

elif exercices == "3":
    print("DIVISION\n")
    division()
    exit()

elif exercices == "4":
    print("")

elif exercices == "5":
    print("")

elif exercices == "6":
    print("")

elif exercices == "7":
    print("")

else:
    exit()