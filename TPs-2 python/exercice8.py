liste=[5,6,1,4,5,8,5,6,8,7,2]

nbr=int(input("saisir un nombre à chercher : "))

occ = []
for i in range(len(liste)):
    if liste[i] == nbr:
        occ.append(i)

print(f"le nombre d'occurance de nombre{nbr} est {len(occ)} des indices {occ} ")