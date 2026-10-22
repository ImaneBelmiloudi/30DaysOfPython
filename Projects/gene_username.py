nom = str(input("entrer ton nom :"))
prénom = str(input("entrer ton prénom :"))
n_nom=nom.lower()
n_prénom =prénom[:3].lower()

username = n_prénom + n_nom + "1"
print(f"le nom est {n_nom} et prénom est : {n_prénom}")
print("Username généré :",username)