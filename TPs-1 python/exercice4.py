second=int(input("saisir le nombre en second : "))

heure=(second)//3600
minute=(second%3600)//60
second=(second%3600)%60

print(str(heure)+" h et "+str(minute)+"  min et "+str(second)+" sec...")
