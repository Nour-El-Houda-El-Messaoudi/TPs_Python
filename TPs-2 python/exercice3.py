import random
random_number=random.randint(1,100)
num =int(input ("saisir un nombre entre 1 et 100 :"))

print("On va jouer a un petit jeu,je vais générer un nombre entre 1 et 100 et tu vas le devinez en en 7 essais ****\n")

for t in range(7):
    if random_number==num:
        print(f"Bravo {random_number} est le nombre que j'ai choisit")
        print(f" vous avez deviné {t} essais")
        break
    elif num > 100 or num < 1:
        print("Oups, vous avez saisi un nombre en dehors de l'intervalle")
        continue
    elif random_number > num :
        print("Oups, entrer un nombre plus grand !")
    elif random_number < num :
        print("Oups, entrer un nombre plus petit !")
    num=int(input(""))

if(num != random_number):
    print("vous n'avez pas devinez le nombre en 7 essais :(")
