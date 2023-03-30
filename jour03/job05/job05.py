#Biblio re pour utiliser des expressions régulières
import re
#Biblio pour vérifier l'existance du fichier
import os
#Biblio pour histogramme
import matplotlib.pyplot as plt

#Fichier à lire
data_file = "jour03/job01/data.txt"

#Fonction de vérification d'existence du fichier
def doesExist(file):
    if os.path.exists(file):
        print(f"{file} existe." )
    else:
        print(f"{file} n'existe pas")

#Vérification existence ficheir
doesExist(data_file)

#Tableau du nombre de mots de x lettres
words_length = {}

#Ouverture du fichier data.txt pour lecture
with open(data_file, 'r') as file:
    #Lecture
    file_content = file.read()
    #Expression régulière pour les mots
    words = re.findall(r'\b\w+\b', file_content)
    #Compteur
    words_number = 0

    #Boucle sur les mots pour récupérer leur longueur et increménter leur quantité
    for word in words:
        length = len(word)
        if length in words_length:
            words_length[length] +=1
        else:
            words_length[length] = 1

#On fait le total des valeurs du tableau
total = sum(words_length.number.values())
#Tableau pour les pourcentages
percentages = {}
#Parcours du tableau 
for length, count in words_length.items():
    percentages[length] =  (count / total)*100

# Générer l'histogramme avec Matplotlib
plt.bar(percentages.keys(), percentages.values())
plt.title("Pourcentage d'apparition de chaque taille de mot")
plt.xlabel("Taille de mot")
plt.ylabel("Pourcentage")
plt.show()






    
    