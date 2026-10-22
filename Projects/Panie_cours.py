panier = [
    ("stylo",2,4)
    ("crayon",2,2)
    ("gomme",5,1)
]
# Total à payer
total = 0
for article in panier : 
    prix = article[1]
    quantité=article[2]
    total += prix * quantité

print("Total à payer :",total)

# Produit le plus cher 
prix_max = 0
nom_produit_cher = ""
for article in panier : 
    if article[1] > prix_max:
        prix_max = article[1]
        nom_produit_cher=article[0]

print("Produit le plus cher",nom_produit_cher,"à",prix_max,"dh")

#Nombre d'articles
print("Nombre d'articles :",len(panier))


