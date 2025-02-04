import os                             # N'enlevez pas ces lignes.
os.chdir(os.path.dirname(__file__))   # Elles permettent de se positionner dans le répertoire de ce script

# Importez csv
import csv

# Dans le fichier "Ex5 Stages.csv", vous avez une liste de stages en programmation et en TI

# Vous voulez extraire les stages de TI et les mettres dans un nouveau fichier spécifique aux stages de TI

 

# Regardez le contenu du fichier "Ex5 Stages.csv"
# 
#          Observez que dans ce fichier, la première ligne comprends les en-têtes de colonne 
#                  Compagnie|Ville|Voie de sortie
#          La valeur de la Voie de sortie est soit 'Prog', soit 'TI'
#          
#          Il vous faudra créer un autre fichier appelé "Ex5 Stages TI.csv" dans lequel vous écrirez les stages en TI seulement
# 
#  Si vous êtes à l'aise en programmation allez-y
#  Des instructions détaillées sont données plus bas


ficher_a_lire = os.path.join("csvs", "Ex5 Stages.csv")

stage = "C:\\Users\\6297003\\Desktop\\R03 Exercices Depart\\csvs\\Ex5 Stages.csv"






















# INSTRUCTIONS DÉTAILLÉES
# Ouvrez en lecture le fichier "Ex5 Stages.csv", en utilisant l'encoding utf-8   
    # Crée un csv.reader() avec le delimiter='|'  
with open(stage, 'r', encoding='utf-8') as csv_fileRead:
    csv_read = csv.reader(csv_fileRead, delimiter='|')
    # Ouvrez en écriture le fichier "Ex5 Stages TI.csv" , en utilisant l'encoding utf-8
    with open(stage, 'w', encoding='utf-8') as csv_fileWrite:
        # Créez un csv.writer avec l'encoding utf-8 et le delimiter '\n'
        csv_write = csv.writer(csv_fileWrite, 
                               delimiter='|',
                               lineterminator="\n")
        # Écrivez dans le fichier Ex5 Stages TI.csv les entêtes du premier fichier ( avec writerow() et next())  
        #entete = next(csv_read)
        #csv_write.writerow(entete)
        # Dans votre boucle qui passera à travers les lignes du fichier de stages

        #      Faites un test pour voir si la valeur de la voie de sortie est TI
        #      Si oui, écrivez cette ligne dans le fichier des stages en TI.
        for range in csv_read:
            if "TI" in range:
                csv_write.writerow(range)



