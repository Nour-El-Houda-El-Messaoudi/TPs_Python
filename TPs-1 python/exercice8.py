notes=[12,15.25,13.5,8.75]
coef=[2,1,4,3]
moyenne=0
somme=0
#for t in range(4):
 #   notes[t]=float(input("saisir la note num "+str(t+1)+" :"))
  #  coef[t]=float(input(" le coefficient : de la note num"+ str(t+1) +":"))
 
for i in range(4):
    moyenne=(notes[i]*coef[i])+moyenne
    somme=somme+coef[i]
moyenne=moyenne/somme
for t in range(4):
     print("note "+str(t)+" : "+str(notes[t]))
     print("coefficient : "+str(coef[t]))

if moyenne>=10:
    print("moyenne de ces 4 notes : ",  moyenne," semestre validé")
else:
        print("moyenne de ces 4 notes : ",  moyenne," semestre non validé")


