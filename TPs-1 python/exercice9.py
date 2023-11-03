


total_facture = 0

NomArticle1 = input(" saisir le nom du premier article : ")
QuantiteArticle1 = int(input(" saisir la quantité du premier article : "))
PrixArticle1 = float(input(" saisir le prix du premier article : "))
tva = 0.20 

MontantHTArticle1 = PrixArticle1 * QuantiteArticle1

Montant_TTC_Article1 = MontantHTArticle1 + MontantHTArticle1 * tva

total_facture += Montant_TTC_Article1

NomArticle2 = input(" saisir le nom du deuxième article : ")
QuantiteArticle1 = int(input(" saisir la quantité du deuxième article "))
PrixArticle1 = float(input(" saisir le prix du deuxième article : "))

MontantHTArticle2 = PrixArticle1 * QuantiteArticle1

Montant_TTC_Article2 = MontantHTArticle2 + MontantHTArticle2 * tva

total_facture += Montant_TTC_Article2

print(f" Totale pour l'article {NomArticle1} :  {MontantHTArticle1:.2f} (ht)")
print(f" Totale pour l'article {NomArticle2} :  {MontantHTArticle2:.2f} (ht)")
print(f" Le totale de votre facture est :  {total_facture:.2f} (TTC)")
