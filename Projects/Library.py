catalogue = {
    "LIV-001": {"titre": "Le Petit Prince", "auteur": "Saint-Exupéry", "disponible": True},
    "LIV-002": {"titre": "L'Alchimiste", "auteur": "Paulo Coelho", "disponible": True},
    "LIV-003": {"titre": "1984", "auteur": "George Orwell", "disponible": False},
}
membres = {
    "MEM-001":{"nom":"Sara Alami","emprunts":"[]"},
    "MEM-002":{"nom":"Imane Belmiloudi","emprunts":"[]"}
}
LIMITE_EMPRUNTS =3
historique = []

def afficher_catalogue(catalogue):
    for id_livre, livre in catalogue.items():
        if livre["disponible"]:
            etat = "Disponible"
        else:
            etat = "Emprunté"
        print(id_livre, "|", livre["titre"], "|", livre["auteur"], "|", etat)

def ajouter_livre(catalogue):
    titre= input("Titre :").strip().title()
    auteur= input("Auteur :").strip().title()
    genre= input("Genre :").strip().title()
    
    numero = len(catalogue) + 1
    nouveau_id = f"LIV-{numero:03d}"
    
    catalogue[nouveau_id] = {"titre":titre, "auteur": auteur , "genre":genre,"disponible":True}
    print("Livre ajouté :",nouveau_id)

def rechercher_livre(catalogue):
    mot = input("Mot-clè :").strip().lower()
    trouve = False
    for id_livre, livre in catalogue.items():
        if mot in livre["titre"].lower() or mot in livre["auteur"].lower():
            print(id_livre,"|",livre["titre"],"|",livre["auteur"])
            trouve = True
    if not trouve :
        print("Aucun resultat ")

def inscrie_membre(membres):
    nom = input("Nom :").strip().title()
    if nom == "":
        print("Le nom  ne peut pas etre vide")
        return
    numero = len(membres) + 1
    nouveau_id = f"MEM-{numero:03d}"

    membres[nouveau_id] = {"nom":nom,"emprunts":[]}
    print("Membre inscrit :",nouveau_id)

def emprunter_livre(catalogue, membres,historiques):
    id_membre = input("Membre :").strip().upper()
    id_livre = input("Livre :").strip().upper()
    jour = int(input("Jour :"))
    if id_membre not in membres :
        print("Membre inconnu")
        return
    if id_livre not in catalogue:
        print("Livre inconnu")
        return
    if not catalogue[id_livre]["disponible"]:
        print("Livre dèjà emprunté")
        return
    if len(membres[id_membre]["emprunts"] >= LIMITE_EMPRUNTS ):
        membres[id_membre]["emprunts"].append(id_livre)
        historique.append((id_livre,id_membre,jour))
        print("Emprunt enregistré")
emprunter_livre(catalogue, membres,historique)
afficher_catalogue(catalogue)
print(historique)
inscrie_membre(membres)
print(membres)
rechercher_livre(catalogue)
ajouter_livre(catalogue)

