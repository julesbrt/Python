nMax = 3
i = 0
v1 = []
v2 = []
res=0.0
n = int(input("Quelle est la taille de vos vecteurs [entre 1 et 3] ? "))
while not 1 <= n <= nMax:
    n = int(input("Valeur incorrecte, quelle est la taille de vos vecteurs [entre 1 et 3] ? "))

print("\nSaisie du premier vecteur :")
for i in range(n):
    y = int(input(f"v1[{i}] = "))
    v1.append(y)

print("\nSaisie du premier vecteur :")
for i in range(n):
    y = int(input(f"v2[{i}] = "))
    v2.append(y)

for i in range(n):
    res+= v1[i] * v2[i]

print(f"\nLe produit scalaire de v1 par v2 vaut {res}")