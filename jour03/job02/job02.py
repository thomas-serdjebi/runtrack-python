#Biblio re pour utiliser des expressions régulières
import re
#Biblio pour vérifier l'existance du fichier
import os

data_file = "jour03/job01/data.txt"

def doesExist(file):
    if os.path.exists(file):
        print(f"{file} existe." )
    else:
        print(f"{file} n'existe pas")

doesExist(data_file)

length = int(input("Choisissez la longueur des mots à compter : "))


#Ouverture du fichier data.txt pour elcture
with open(data_file, 'r') as file:
    #Lecture
    file_content = file.read()
    #Expression régulière pour les mots
    words = re.findall(r'\b\w+\b', file_content)
    #Compteur
    words_number = 0
    

    #Parcours les mots et vérifie s'il n'y a pas de caractère spécial
    for word in words:
        if len(word) == length:
            words_number +=1
    
    print(f"{data_file} contient {words_number} mots d'une longueur de {length} caractères.")
    