import string
import matplotlib.pyplot as plt

# Créer un dictionnaire pour stocker le nombre d'occurrences de chaque lettre en début de mot
initial_letter_counts = {}
for letter in string.ascii_lowercase:
    initial_letter_counts[letter] = 0

# Ouvrir le fichier "data.txt" en mode lecture
with open("jour03/job01/data.txt", "r") as file:
    # Parcourir chaque ligne du fichier
    for line in file:
        # Convertir la ligne en minuscules
        line = line.lower()
        # Séparer la ligne en mots
        words = line.split()
        # Parcourir chaque mot
        for word in words:
            # Vérifier que le mot commence par une lettre de l'alphabet anglais
            if word[0] in string.ascii_lowercase:
                # Incrémenter le compteur pour la lettre initiale
                initial_letter_counts[word[0]] += 1

# Calculer le nombre total d'occurrences de chaque lettre en début de mot
total_counts = sum(initial_letter_counts.values())

# Calculer le pourcentage de présence de chaque lettre en début de mot
initial_letter_percentages = {}
for letter, count in initial_letter_counts.items():
    initial_letter_percentages[letter] = count / total_counts * 100

# Générer l'histogramme avec Matplotlib
plt.bar(initial_letter_percentages.keys(), initial_letter_percentages.values())
plt.title("Pourcentage de présence de chaque lettre en début de mot")
plt.xlabel("Lettre")
plt.ylabel("Pourcentage")
plt.show()
