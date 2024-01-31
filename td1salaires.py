# Définition des variables
nb_employes = int(input("Entrez le nombre d'employés : "))
noms = []
salaires = []

# Saisie des données
for i in range(nb_employes):
    nom = input("Entrez le nom de l'employé {} : ".format(i + 1))
    salaire = float(input("Entrez le salaire de l'employé {} : ".format(i + 1)))
    noms.append(nom)
    salaires.append(salaire)

# Recherche de l'employé avec le salaire le plus bas
salaire_min = salaires[0]
index_min = 0
for i in range(1, nb_employes):
    if salaires[i] < salaire_min:
        salaire_min = salaires[i]
        index_min = i

# Recherche de l'employé avec le salaire le plus haut
salaire_max = salaires[0]
index_max = 0
for i in range(1, nb_employes):
    if salaires[i] > salaire_max:
        salaire_max = salaires[i]
        index_max = i

# Affichage des résultats
print("L'employé avec le salaire le plus bas est {} avec un salaire de {}.".format(noms[index_min], salaire_min))
print("L'employé avec le salaire le plus haut est {} avec un salaire de {}.".format(noms[index_max], salaire_max))
