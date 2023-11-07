
temp=[[0,0,0],[0,0,0]]
for i in range(2):
    temp[i][0]=int(input("saisir l'heures. :"))
    temp[i][1]=int(input("saisir les minutes :"))
    temp[i][2]=int(input("saisir les second :"))


def convertion_temps(time) :
    seconde= time[0]*3600+time[1]*60+time[2]
    return seconde

temps_ecoule=convertion_temps(temp[0])-convertion_temps(temp[1])

print(temps_ecoule)
