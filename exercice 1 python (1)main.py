from itertools import product


def table_de_verite(variables, fonction):
    """
    Génère la table de vérité pour la fonction logique donnée avec les variables spécifiées.
    """
    n = len(variables)
    table = list(product([0, 1], repeat=n))

    print("Table de vérité:")
    for row in table:
        context = {variables[i]: row[i] for i in range(n)}
        result = eval(fonction, {}, context)
        print(" | ".join([str(x) for x in row]), "|", int(result))
    return table


def premiere_forme_canonique(variables, table):
    """
    Calcule et affiche la première forme canonique de la fonction logique donnée.
    """
    terms = []
    for row in table:
        if row[-1] == 1:
            term = []
            for i, val in enumerate(row[:-1]):
                if val == 1:
                    term.append(variables[i])
                elif val == 0:
                    term.append(f"~{variables[i]}")
            terms.append(" & ".join(term))
    expression = " | ".join(terms)
    print("\nPremière forme canonique:")
    print(expression)


def deuxieme_forme_canonique(variables, table):
    """
    Calcule et affiche la deuxième forme canonique de la fonction logique donnée.
    """
    terms = []
    for row in table:
        if row[-1] == 0:
            term = []
            for i, val in enumerate(row[:-1]):
                if val == 0:
                    term.append(variables[i])
                elif val == 1:
                    term.append(f"~{variables[i]}")
            terms.append(" | ".join(term))
    expression = " & ".join(terms)
    print("\nDeuxième forme canonique:")
    print(expression)


# Demande à l'utilisateur de saisir la fonction logique et les variables
fonction_logique = input("Entrez la fonction logique en utilisant 'and', 'or' et 'not': ")
variables = input("Entrez les noms des variables séparées par des espaces: ").split()

# Générer et afficher la table de vérité
table = table_de_verite(variables, fonction_logique)

# Calculer et afficher les formes canoniques
premiere_forme_canonique(variables, table)
deuxieme_forme_canonique(variables, table)

