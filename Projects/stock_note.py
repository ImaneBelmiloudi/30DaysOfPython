lista = []
etudiant = {
    "nom":"Ali",
    "notes":[12,15,9]
}
lista.append(etudiant)
choix =""
while choix !="4":
    print("1.Ajouter un étudiant et ses notes")
    print("2.La moyenne d'un étudiant moyenne")
    print("3.Afficher un étudiant avec la meilleure note")
    print("4. Réssayez à nouveau")
    choix = input("Enter votre choix")
    if choix == "1":
        nom =  input("Ajouter le nom d'étudiant :")
        note1 = int(input("Enter note1 :"))
        note2 = int(input("Enter note2 :"))
        note3 = int(input("Enter note3 :"))
        notes = [note1,note2,note3]
        nouveau_etudiant = {"nom":nom , "notes":notes}
        print(f"nom : {nouveau_etudiant['nom']} , notes : {nouveau_etudiant['notes']}")
        lista.append(nouveau_etudiant)
        print("Vos informations sont ajoutés !!!")
    if choix == "2":
        nom = input("Entre le nom de l'étudiant/moyenne :")
        trouve = False
        for etudiant in lista :
            if etudiant['nom'] == nom :
                moyenne = sum(etudiant['notes']) / len (etudiant['notes'])
                print(f"La moyenne de {nom} est : {moyenne}")
                trouve = True
            if not trouve:
                print("Ce nom est introuvable")