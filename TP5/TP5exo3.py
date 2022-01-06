m=input("Entrez un mot ou une phrase : ")
mot=m.lower()
mots=[]
for i in mot:
    if i.isalpha():
        mots.append(i)

if str(mots) == str(mots[::-1]):
    print("Le mot est un palindrome")
else :
    print("Le mot n'est pas un palindrome")
