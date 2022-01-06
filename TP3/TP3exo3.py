import random

rand = random.randint(0, 100)
x=1
while 0<rand<100:
    nb = int(input(f"Entrez un nombre entre 0 et 100 : "))
    if not 0 <= nb <= 100:
        print("Mauvaise valeur, entrez un nombre entier entre 0 et 100")

    if rand<nb:
        print("Plus petit")
        x+=1
    elif rand>nb:
        print("Plus grand")
        x+=1
    else:
        print("Valeur correct, le nombre d'essaie est de : ",x)