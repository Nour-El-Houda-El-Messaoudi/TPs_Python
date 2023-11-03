liste=[1,2,3,4,6,7,8,9,10,11]
val = 5
i=0
while len(liste) > i and liste[i]<val :
    i+=1

liste.insert(i,val)

print(liste)
