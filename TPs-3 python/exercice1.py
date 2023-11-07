
def somme( n, m):
    som=0
    if n > m :
        c=n
        n=m
        m=c  
    while n<=m :
        som+=n 
        n+=1
    return som

n=int(input("saisir n :"))
m=int(input("\nsaisir m :"))

print(somme(n,m))