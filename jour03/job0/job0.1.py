#Ouvre "output.txt
with open("output.txt", "r") as file:
    #Lis le contenu
    file_content = file.read()
    print(file_content)