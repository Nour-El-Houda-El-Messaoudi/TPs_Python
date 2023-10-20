distance = float(input("Entrez la distance en kilomètres : "))
temps = float(input("Entrez le temps en minutes : "))
temps_sec = temps * 60
distance_mtr = distance * 1000
vitesse_mps = distance_mtr / temps_sec
print("La vitesse est de", vitesse_mps, "mètres par seconde.")
