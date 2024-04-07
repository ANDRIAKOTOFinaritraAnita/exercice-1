def table_de_verite(fonction_logique):
    print("Table de vérité :")
    print("x | y | f(x, y)")
    print("---------")
    for x in [0, 1]:
        for y in [0, 1]:
            resultat = fonction_logique(x, y)
            print(f"{x} | {y} | {resultat}")
    print("---------")

def premiere_forme_canonique(fonction_logique):
    termes = []
    for x in [0, 1]:
        for y in [0, 1]:
            if fonction_logique(x, y) == 1:
                termes.append(f"(x{'\' ' if x == 0 else ''}y{'\' ' if y == 0 else ''})")
    print("Première forme canonique :")
    if len(termes) == 0:
        print("1")
    else:
        print(" + ".join(termes))

def deuxieme_forme_canonique(fonction_logique):
    termes = []
    for x in [0, 1]:
        for y in [0, 1]:
            if fonction_logique(x, y) == 0:
                termes.append(f"(x{' ' if x == 0 else '\' '}+ y{' ' if y == 0 else '\' '})")
    print("Deuxième forme canonique :")
    if len(termes) == 0:
        print("1")
    else:
        print(" * ".join(termes))

def principal():
    # Demander à l'utilisateur d'entrer la fonction logique
    fonction = input("Entrez la fonction logique (en utilisant les opérateurs and, or, not, et les variables x et y) : ")
    try:
        # Convertir la chaîne entrée en une fonction logique
        fonction_logique = eval(f"lambda x, y: {fonction}")
    except:
        print("Erreur: Fonction logique invalide.")
        return

    # Afficher les résultats
    table_de_verite(fonction_logique)
    premiere_forme_canonique(fonction_logique)
    deuxieme_forme_canonique(fonction_logique)

if __name__ == "__main__":
    principal()
