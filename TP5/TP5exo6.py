T = input("Entrez T: ")

def longueur(n):
    len = 0
    for i in n:
        len += 1
    return len
print(f"Longeur de T: {longueur(T)}")

def voyelle(n):
    voy = ('a', 'e', 'i', 'o', 'u', 'y')
    count = 0
    for i in n:
        if i in voy:
            count += 1
    return count
print(f"Pourcentage de voyelles: {round(voyelle(T) / longueur(T) * 100, 2)}")


def rech(n, x):
    for i in range(longueur(n)):
        if n[i:i + longueur(x)] == x:
            return i
    return -1
print(f"Première occurence de 'wagon': {rech(T, 'wagon')}")

def nboccur(n, x):
    count = 0
    for i in range(longueur(n)):
        if n[i:i + longueur(x)] == x:
            count += 1
    return count
print(f"Occurences de 'wagon': {nboccur(T, 'wagon')}")