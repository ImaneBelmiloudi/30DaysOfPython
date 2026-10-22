phrase = "I am good in coding and I wanna be a machine learning engineer"
mots = phrase.split()
nombre_mots = len(mots)
phrase_nettoyee = phrase.lowe().replace("","")
est_palindrome = phrase_nettoyee == phrase_nettoyee[::-1]
if est_palindrome :
    print("C'est un palindrome")
else :
    print("Ce n'est pas un palindrome")
print("Nombre de mots",nombre_mots)
print(len(phrase))
print(phrase.upper())
print(phrase.lower())