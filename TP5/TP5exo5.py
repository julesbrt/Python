salaire=int(input("Entrer votre salaire horaire :"))
h=int(input("Entrer le nombre d'heure travaillé :"))
paie = 0
majun=0
majdeux=0

if h<=160:
    paie=salaire*h

elif h<=200:
    majun=(h-160)*salaire*1.25+160*salaire

elif h>200:
    majdeux=(h-200)*salaire*1.50+40*salaire*1.25+160*salaire

paie+=majun+majdeux

print(paie)