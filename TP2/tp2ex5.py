a=int(input("Entrez un nombre entier :"))
if a%2 == 0 :
    if a > 0:
        print("Le nombre est positif et pair")
    elif a < 0:
        print("Le nombre est négatif et pair")
    else:
        print("le nombre est zéro (et il est pair)")
else:
    if a > 0:
        print("Le nombre est positif et impair")
    else :
        print("Le nombre est négatif et impair")
