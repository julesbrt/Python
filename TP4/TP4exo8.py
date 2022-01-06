ledico = {}
ledico['firstname'] = 'julo'
ledico['name'] = 'brutscho'
ledico['promo'] = 'Réseaux Télécom 2021'
ledico['group'] = 'RT111'

deuxdico = {}
deuxdico['firstname'] = 'Thomas'
deuxdico['name'] = 'Bilger'
deuxdico['promo'] = 'Réseaux Télécom 2021'
deuxdico['group'] = 'RT111'

troisdico = {}
troisdico['firstname'] = 'Massimo'
troisdico['name'] = 'Auréli'
troisdico['promo'] = 'Réseaux Télécom 2021'
troisdico['group'] = 'RT112'

quattrodico = {}
quattrodico['firstname'] = 'Louiss'
quattrodico['name'] = 'Desvernoiss'
quattrodico['promo'] = 'Réseaux Télécom 2021'
quattrodico['group'] = 'RT111'

binome = (ledico.values(), deuxdico.values())
binome2 = (troisdico, quattrodico)

tp111 = {}
tp111['1'] = binome
tp111['2'] = binome2

for a in range(1, 3):
    print("Le binome N°{} est composé de {}".format(a, tp111[f'{a}']))
"""
for a in tp111:
    temp = tp111[a][0]
    temp2 = tp111[a][1]
    print("Le binome N°{} est composé de {} {} {} {} et de {} {} {} {} ".format(a, temp['firstname'],temp['name'],temp['promo'],temp['group'], temp2['firstname'],temp2['name'],temp2['promo'],temp2['group']))
"""
