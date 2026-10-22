import random
mots = ["python","data","algorithme","ordinateur","intelligence"]
mot = random.choice(mots)

affichage = ["_"] * len(mot)
vies = 6
lettres_essayees = []

dessins =[
    "",
    " 0",
    " 0\n |",
    " O\n/|",
    " O\n/|\\",
    " O\n/|\\\n/",
    " O\n/|\\\n/ \\",
]
while vies > 0 and "_" in affichage:
    print("\n"+ " ".join(affichage))
    lettre = input("Entre une lettre :").lower()

    if len(lettre) != 1 or not lettre.isalpha():
        print("Entre une seule lettre, s'il te plait")
        continue
    if lettre in lettres_essayees:
        print("Tu déjà essayé cette lettre")
        continue
    lettres_essayees.append(lettre)

    if lettre in mot  :
        for i in range (len(mot)):
            if mot[i] == lettre :
                affichage[i] = lettre
        print("Bravo, bonne lettre !")
    else :
        vies = 1
        print(f"Raté ! Il te reste {vies} vies")
        print(dessins[6 - vies])
if "_" not in affichage :
    print("\nGagné ! Le mot ètait :",mot)
else:
    print("\nPerdu .... ! Le mot ètait :",mot)
