chiffre=input("saisir un chiffre : ")
concat=""
resultat=0
for t in range(4):

    for i in range(t+1):

        concat+=chiffre
    #cette condition pour ne pas ajouter '+' à la fin du chiffre
    if t==3:
        print(concat,end="")
    else:  
        print(concat+"+",end="")
    resultat+=int(concat)
    concat=""
    

print(f"={resultat}")
    
