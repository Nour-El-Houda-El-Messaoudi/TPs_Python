taux_euro_to_mad = 10.86
taux_mad_to_euro = 0.092
nombres=[]
montant=0

direction_de_convertion=int (input(" saisir la direction de (1 : si MAD to euro ) (0 : si euro to MAD) :"))
while montant>=0 :
    try :
        montant = float(input("sisir un montant pour s'arreter entrer un montant négatif : "))
        if montant >= 0:
            nombres.append(montant)
    except ValueError:
        print("le nombre est invalid :(")
        
valeurs_final = []
if direction_de_convertion == 1:
    for i in range(len(nombres)):
        valeur_convertie = nombres[i] * taux_mad_to_euro
        valeurs_final.append(valeur_convertie)
        print(f"{nombres[i]} MAD est équivalent à {valeur_convertie} euro.")
elif direction_de_convertion == 0:
    for i in range(len(nombres)):
        valeur_convertie = nombres[i] * taux_euro_to_mad
        valeurs_final.append(valeur_convertie)
        print(f"{nombres[i]} euro est équivalent à {valeur_convertie} MAD.")
else:
    print("Direction de conversion invalide.")
    