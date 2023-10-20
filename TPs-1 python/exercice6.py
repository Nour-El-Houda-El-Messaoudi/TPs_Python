premier = int(input("saisir le preminer nombre :"))
deuxieme = int(input("saisir le deuxieme nombre : "))

if ( ( premier < 0 & deuxieme < 0) or( premier >0 & deuxieme > 0 ) ):
    print(" le produit est positif")
elif premier == 0 or deuxieme== 0:
    print("Le produit est nul")
else:
    print(" le produit est négatif")