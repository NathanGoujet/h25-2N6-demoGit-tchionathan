import os                             # N'enlevez pas ces lignes.
os.chdir(os.path.dirname(__file__))   # Elles permettent de se positionner dans le répertoire de ce script

# Importez csv
import csv

os.chdir("C:\\Users\\6297003\\Documents\\GitHub\\h25-2N6-demoGit-tchionathan\\R03 Exercices Depart\\csvs\\")

# Regardez le contenu du fichier "Ex7 Lan Party.csv"
with open("Ex7 Lan Party.csv", 'r', encoding='UTF-8') as csv_read:
    csv_read = csv.reader(csv_read,
                          delimiter=';')
#          Observez que dans ce fichier, la première ligne comprends les en-têtes de colonne 
#                 Lan Party;Top 1;Top 2; Top 3
#          Top 1, Top 2 et Top 3 sont les jeux les plus populaires dans chaque Lan Party
#          
#          Vous aimez jouer à Valorant
#          Imprimez la liste des Lan Party dans lesquels votre jeu préféré est parmi leurs Tops
    for ligne in csv_read:
        if  "Valorant" in ligne:
            print(ligne)
# 
#          Aucune instruction détaillée n'est donnée plus bas




