noms = []
for i in range(2):
    noms.append((input(f"Nom : ").upper(),
                input(f"Prénom : ").capitalize()))
noms.sort()
for temp in noms:
    print(f"{temp[1]} {temp[0]}")