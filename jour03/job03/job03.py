#Biblio re pour utiliser des expressions régulières
import re
#Biblio pour vérifier l'existance du fichier
import os
#Biblio pour histogramme
import matplotlib.pyplot as plt

data_file = "jour03/job01/data.txt"

def doesExist(file):
    if os.path.exists(file):
        print(f"{file} existe." )
    else:
        print(f"{file} n'existe pas")

doesExist(data_file)


#Ouverture du fichier data.txt pour elcture
with open(data_file, 'r') as file:
    #Lecture + conversion de toutes les lettres en minuscules
    file_content = file.read().lower()
    #Expression régulière pour les lettres
    letters = re.findall(r'[a-z]', file_content)
    #Compteur
    letter_number = {}
    for letter in letters:
        if letter in letter_number:
            letter_number[letter] += 1
        else:
            letter_number[letter] = 1

#Calcul du pourcentage d'apparition
total = sum(letter_number.values())
percentages = {}
for letter, number in letter_number.items():
    percentages[letter] = (number / total) * 100

#Histogramme
plt.bar(percentages.keys(), percentages.values())
plt.title("Pourcentage d'apparition de chaque lettre dans le fichier data.txt")
plt.xlabel("Lettres")
plt.ylabel("Pourcentage")
plt.show()
    