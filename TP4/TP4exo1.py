nb=float(input("Vous cherchez la table de multiplication de quel nombre ? : "))
t=[]
for i in range (10):
    t.append(nb*i)
    print("{} * {} = {:.2f}".format(nb,i,t[i]))