#Demande à l'utilisateur de saisir une chaîne de caractères
user_input = input("Ecrivez une phrase : ")

#Ouvre le fichier "output.txt" pour écriture
with open("output.txt", "w") as file:
    #Ecris la phrase saisie par le user
    file.write(user_input)
