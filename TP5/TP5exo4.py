som=int(input("Entrer la somme d'argent :"))
temp=som
bcent=0
bcinq=0
bdix=0
pdeux=0
pun=0

while som >= 100:
    bcent+=1
    som-=100

while som >= 50:
    bcinq+=1
    som-=50

while som >= 10:
    bdix+=1
    som-=10

while som >= 2:
    pdeux+=1
    som-=2

while som >= 1:
    pun+=1
    som-=1

print(f"{temp} euros, c’est donc {bcent} billets de 100, {bcinq} de 50, {bdix} de 10, {pdeux} pièces de 2 et {pun} pièce 1.")