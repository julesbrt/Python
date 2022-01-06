notes = []
for i in range(5):
    notes.append(input(f"Veuillez entrer la note du module {i + 1} et le coefficient correspondant :"))
    if i < 8 :
        k = 1
print(notes)
print(enumerate(notes))
for i, item in enumerate(notes):
    temp = item.split(" ")
    notes[i] = (float(temp[0]), int(temp[1]))

print(notes)
hautdiv, basdiv = 0.0, 0
for note, coef in notes:
    hautdiv += note * coef
    basdiv += coef

moy = (hautdiv / basdiv)
print(f"La moyenne est de {round(moy, 2)}")
if moy >= 10 and k != 1 :
    print("L'étudiant est admis")
else:
    print("L'étudiant n'est pas admis")

