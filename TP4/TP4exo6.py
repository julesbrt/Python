tab = []
nMax = 10
i = 0
n = int(input("Quelle est la taille de votre liste [entre 1 et 10] ? "))
while not 1 <= n <= nMax:
    n = int(input("Valeur incorrecte, quelle est la taille de votre liste [entre 1 et 10] ? "))

print("\nEntrer les valeurs de la liste : ")
for i in range(n):
    y = int(input(f"[{i}] = "))
    tab.append(y)


print("\n",tab)

for i in range(len(tab)):
    temp = tab[i]

    index = 0
    for j in range(i, len(tab)):
        if tab[j] < temp:
            temp = tab[j]
            index = j

    if index != 0:
        tab[index] = tab[i]
        tab[i] = temp
    print(f"Phase {i}: {tab}")

