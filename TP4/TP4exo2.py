nbetud=int(input("Donnez le nombre d'etudiants : "))
moy = 0.0
notes = []
for i in range(nbetud):
    temp = float(input(f"Donnez la note de l'étudiant {i+1}: "))
    while not 0<=temp<=20:
        print("La note n'est pas entre 0 et 20, veuillez en entrer une nouvelle :")
        temp = float(input(f"Donnez la note de l'étudiant {i + 1}: "))
    notes.append(temp)
    moy+=notes[i]

moy/=nbetud
print(f"\nMoyenne de clase : {moy}\n")

print("Numéro de l'Etudiant | note | ecart a la moyenne")
for i in range(nbetud):
    print(i+1,"|",notes[i],"|",notes[i]-moy)