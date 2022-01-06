debut=int(input("Donnez l’heure de début de la location (un entier) :"))
fin=int(input("Donnez l’heure de fin de la location (un entier) :"))
while True:
    if not 0<debut<=24 or not 10<=fin<=24:
        print("Les heures doivent être comprises entre 0 et 24 ! \n")
        debut = int(input("Donnez l’heure de début de la location (un entier) :"))
        fin = int(input("Donnez l’heure de fin de la location (un entier) :"))

    elif debut==fin:
        print(" Attention ! l’heure de fin est identique à l’heure de début.\n")
        debut = int(input("Donnez l’heure de début de la location (un entier) :"))
        fin = int(input("Donnez l’heure de fin de la location (un entier) :"))

    elif debut>fin:
        print(" Attention ! le début de la location est après la fin ...\n")
        debut = int(input("Donnez l’heure de début de la location (un entier) :"))
        fin = int(input("Donnez l’heure de fin de la location (un entier) :"))

    else:
        break

location = []
for i in range(debut, fin): location.append(i)

UnEuro = 0
DeuxEuros = 0
for i in location:
        if i in range(7, 17):
            UnEuro += 1
        else:
            DeuxEuros += 1

if DeuxEuros != 0: print(f"\t- {DeuxEuros} heure(s) au tarif de 1€.")
if UnEuro != 0: print(f"\t- {UnEuro} heure(s) au tarif de 2€.")
print(f"Le montant total à payer de {DeuxEuros + 2 * UnEuro}€.")

