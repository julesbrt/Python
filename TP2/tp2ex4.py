BASE=4
fromage=800.0
qtfromage=fromage/BASE
ail=2.0
qtail=ail/BASE
eau=2.0
qteau=eau/BASE
pain=400.0
qtpain=pain/BASE

personnes=int(input("entrez le nombre de personne(s) conviée(s) à la fondue :"))
fromage=qtfromage*personnes
eau=qteau*personnes
ail=qtail*personnes
pain=qtpain*personnes
print("Pour faire une fondue fribourgeoise pour {} personnes, il vous faut : \n -{} gr de fromage \n -{} dl d'eau \n -{} gousse d'ail \n -{} gr de pain".format(personnes, fromage, eau, ail, pain))

