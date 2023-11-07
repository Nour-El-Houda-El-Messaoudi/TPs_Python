def conversion_distance(distance):
    return (distance[0]*1000)+distance[1]+distance[2]/100

def convertion_temps(time) :
    seconde= time[0]*3600+time[1]*60+time[2]
    return seconde


heure=int(input("saisir l'heures. :"))
minu=int(input("saisir les minutes :"))
sec=int(input("saisir les second :"))


km=int(input("saisir KM :"))
m=int(input("saisir M :"))
cm=int(input("saisir CM :"))

distance=[km,m,cm]
temps=[heure,minu,sec]
vitesse=float(conversion_distance(distance)/convertion_temps(temps))


print(f"la vitesse est {vitesse} m/s")











