import string
import matplotlib.pyplot as plt

# Créer un dictionnaire pour stocker le nombre d'occurrences de chaque lettre suivante
next_letter_counts = {}
for letter in string.ascii_lowercase:
    next_letter_counts[letter] = {}

# Ouvrir le fichier "data.txt" en mode lecture
with open("data.txt", "r") as file:
    # Parcourir chaque ligne du fichier
    for line in file:
        # Convertir la ligne en minuscules
        line = line.lower()
        # Parcourir chaque caractère de la ligne
        for i in range(len(line) - 1):
            current_letter = line[i]
            next_letter = line[i+1]
            # Incrémenter le compteur pour la lettre suivante
            if next_letter in next_letter_counts[current_letter]:
                next_letter_counts[current_letter][next_letter] += 1
            else:
                next_letter_counts[current_letter][next_letter] = 1

# Calculer le nombre total d'occurrences de chaque lettre
total_counts = {}
for letter in string.ascii_lowercase:
    total_counts[letter] = sum(next_letter_counts[letter].values())

# Calculer le pourcentage d'apparition de chaque lettre suivante
next_letter_percentages = {}
for letter in string.ascii_lowercase:
    next_letter_percentages[letter] = {}
    for next_letter, count in next_letter_counts[letter].items():
        next_letter_percentages[letter][next_letter] = count / total_counts[letter] * 100

# Générer le graphique de courbes superposées avec Matplotlib
for letter in string.ascii_lowercase:
    plt.plot(list(next_letter_percentages[letter].keys()), list(next_letter_percentages[letter].values()), label=letter)

plt.title("Pourcentage d'apparition de chaque lettre suivante")
plt.xlabel("Lettre suivante")
plt.ylabel("Pourcentage")
plt.legend()
plt.show()
