liste=[5,65,4,5,4,1,-2,3,5,1,5]
val=int(input("saisir un nombre à supprimé :"))
i=0
for t in liste:
    if val==t:
        liste.pop(i)
    i+=1

print(liste)