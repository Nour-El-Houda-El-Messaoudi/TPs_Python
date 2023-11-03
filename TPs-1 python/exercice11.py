
Poids=float(input("saisie votre poid en kg : "))
taille=float(input("saisie votre taille en cm : "))
IMC=10000*Poids/(taille*taille)

print(f"\nTon IMC EST {IMC:.2f} vous etes :")

if  16.5 > IMC :
     print( "Famine")
elif 16.5 <= IMC < 18.5:
    print( "Maigreur")
elif 18.5 <= IMC < 25:
    print("Corpulence normale")
elif 25 <= IMC < 30:

    print( "Surpoids")
elif 30 <= IMC < 35:
    print( "Obésité modérée")
elif 35 <= IMC < 40:
    print( "Obésité sévère")
elif IMC >= 40:
    print( "Obésité morbide ou massive")



   