import os                             # N'enlevez pas ces lignes.
os.chdir(os.path.dirname(__file__))   # Elles permettent de se positionner dans le répertoire de ce script

import csv


# Tu as toujours rêvé de travailler un jour pour le CH
# Tu as vu une job en TI, 
#           Analyste, soutien technique réseau

# Le fichier Ex3 Competences.csv contient la liste des compétences qu'ils demandent, 
# #         avec le niveau et le fait que cette compétence est exigée ou plutôt un atout
# Bien que tu n'as pas encore fini tes études tu veux imprimer ici les compétences qui sont exigées 
# afin de bien développer ces compétences pour qu'éventuellement tu puisses entrer dans cette entreprise

#  Si vous êtes à l'aise en programmation allez-y
#  Des instructions détaillées sont données plus bas











os.chdir("C:\\Users\\6297003\\Documents\\GitHub\\h25-2N6-demoGit-tchionathan\\R03 Exercices Depart\\csvs\\")

# INSTRUCTIONS DÉTAILLÉES
#Ouvrez en lecture le fichier Ex6 Competences.csv
with open("Ex6 competences.csv", "r", encoding="UTF-8") as csv_read:
    csv_read = csv.reader(csv_read,
                          delimiter='/')
#avec l'encodage et le delimiter requis
#Imprimez la première ligne
    
#Faites une boucle pour passer à travers chacune des lignes du fichier
    for ligne in csv_read:
        if "Exigé" in ligne:
            print(ligne)
#Si l'exigence est  'Exigé' imprimez cette ligne
