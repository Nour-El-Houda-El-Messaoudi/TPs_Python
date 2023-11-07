km=2
m=0
cm=0
distance=[km,m,cm]
def conversion_distance(distance):
    return (distance[0]*1000)+distance[1]+distance[2]/100


print(conversion_distance(distance))