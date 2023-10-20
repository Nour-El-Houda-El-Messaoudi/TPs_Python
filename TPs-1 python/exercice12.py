GrilleTarifaire ={
    'A': {'tarif_horaire': 200, 'prime': 1000, 'heures_prime': 20},
    'B': {'tarif_horaire': 150, 'prime': 800, 'heures_prime': 20},
    'C': {'tarif_horaire': 120, 'prime': 500, 'heures_prime': 15},
    'D': {'tarif_horaire': 100, 'prime': 350, 'heures_prime': 15},
    'E': {'tarif_horaire': 80, 'prime': 100, 'heures_prime': 10}   }

grade = input(" saisir le grade de l'employé : ")
HeuresTravailler = int(input(" saisir le nombre d'heures travailler : "))

if grade in GrilleTarifaire:
    tarif_horaire = GrilleTarifaire[grade]['tarif_horaire']
    prime = GrilleTarifaire[grade]['prime']
    heures_prime = GrilleTarifaire[grade]['heures_prime']
    salaire = (tarif_horaire * HeuresTravailler) + (prime * (HeuresTravailler // heures_prime))
    
    print(f" Le salaire de l'employé de cette société est  {salaire} dh.")
else:
    print(" Le grade que vous avez entrer est invalid")
