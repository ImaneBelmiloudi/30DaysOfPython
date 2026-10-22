contacts = []
dict1 = {
    "nom":"Ali",
    "telephone":"06123456789",
}
dict2 = {
    "nom":"Sara",
    "telephone":"06098765413"
}
# tpl = ("travail","urgent")
contacts.append(dict1)
contacts.append(dict2)
# contacts.append(tpl)
for contact in contacts:
    print(f"Nom :{contact['nom']}- Téléphone :{contact['telephone']}")

choix = ""
while choix != "3":
    print("1. Ajouter un contact")
    print("2. Afficher les contacts")
    print("3. Quitter")
    choix = input("Ton choix :")
    if choix == "1":
        nom = input("Nom de contact")
        telephone = input("Téléphone du contact :")
        nouveau_contact = {"nom":nom,"telephone":telephone}
        contacts.append(nouveau_contact)
        print("Contact ajouté")
    elif choix == "2":
        for contact in contacts:
            print(f"Nom :{contact['nom']}- Téléphone :{contact['telephone']}")

    elif choix == "3":
        print("Au revoir !")
    else:
        print("Choix invalide, Réssayez")