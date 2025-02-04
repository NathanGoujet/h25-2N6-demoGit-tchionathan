# importez os
import os
# # allez dans le dossier Ex3 Videos
os.chdir("C:\\Users\\6297003\\Desktop\\R03 Exercices Depart\\Ex3 Videos\\")
# # avec la boucle for, passez à travers chacun des dossiers de os.listdir()
for toutdos in os.getcwd():
    toutdos = os.listdir()
# #     utilisez os.path.splitext pour obtenir le filename et l'extension
    path = "C:\\Users\\6297003\\Desktop\\R03 Exercices Depart\\Ex3 Videos\\"
    os.path.splitext(toutdos)
# #     utilisez split sur le filename pour obtenir le titre, le cours et le numéro du cours
    os.path.split("C:\\Users\\6297003\\Desktop\\R03 Exercices Depart\\Ex3 Videos\\")
# #     utilisez strip pour enlever les espaces qui pourraient rester pour le titre et le numéro
    path.strip()
# #     en plus utilisez zfill pour remplir le numéro de sorte que 1 deviendra 01
    path.zfill()
# #     recréez le nouveau nom de fichier#   utliser os.rename pour renommer le fichier
    

