taille=int(input("saisir la taille du triangle :"))

for i in range(taille):

    for j in range(1+i):
        print(" * ",end="")
    print("\n")


for i in range(taille):

    for j in range(1+i):
        print(i+1,end="")
    print("\n")

    