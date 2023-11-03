


a = float(input("Saisissez le premier nombre : "))
b = float(input("Saisissez le deuxième nombre : "))


operation = input("Saisissez l'opération (+, -, *, /) : ")

if operation == "+":
    print("Résultat : ",a+b )
elif operation == "-":
    print("Résultat : ",a-b )
elif operation == "*":
    print("Résultat : ",a*b )
elif operation == "/":
    if b==0:
        print("on ne peut pas diviser sur 0")
    else:
        print("Résultat : ",a/b )
else:
    print("operation inconnue")

