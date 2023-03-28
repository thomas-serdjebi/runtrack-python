from job0 import Personne
from job01 import Livre
from job01 import Auteur

class Client(Personne):
    def __init__(self, nom, prenom):
        super().__init__(nom, prenom)
        self._livres = []

    def ajouterLivre(self, livre):
        self._livres.append(livre)
    
    def rendreTousLivres(self):
        self._livres = []

    def get_collectionLivres(self):
        return self._livres
        

class Bibliotheque:
    def __init__(self, nom):
        self._nom = nom
        self._catalogue = {}

    def get_nom(self):
        return self._nom

    def get_catalogue(self):
        return self._catalogue
    
    def set_nom(self, nom):
        self._nom = nom

    def set_catalogue(self, catalogue):
        self._catalogue = catalogue

    def acheterLivre(self, auteur, titre, quantite):
        for livre in auteur.get_oeuvre():
            if livre.get_titre() == titre:
                if titre in self._catalogue:
                    self._catalogue[titre] +=quantite
                else: 
                    self._catalogue[titre] = quantite
                print(f"{quantite} exemplaires de {titre} ajoutés au catalogue de la biliothèque")
                return
        print(f"{titre} n'est pas dans l'oeuvre de {auteur.get_nom()}.")

    def inventaire(self):
        print("Inventaire de la biliothèque : ")
        for titre, quantite in self._catalogue.items():
            print(f" - {titre} : {quantite} exemplaires")
    
    def louer(self, client, titre):
        if titre in self._catalogue and self._catalogue[titre] > 0:
            client.ajouterLivre(titre)
            self._catalogue[titre] -= 1
            print(f"{titre} loué avec succès")
        else:
            print(f"{titre} n'est plus disponible.")


    def rendreLivres(self, client):
        for livre in client.get_collectionLivres():
            print(livre)
            if livre in self._catalogue:
                self._catalogue[livre] += 1
            else:
                self._catalogue[livre] = 1
        client.rendreTousLivres()
        print("Les livres ont été rendus avec succès par " + client._prenom)



# création d'un client
client1 = Client("Durand", "Marie")
client2 = Client("Patrick", "Sebastien")
client3 = Client("Abel", "Postman")

biblio1 = Bibliotheque("Alcasar")

auteur1 = Auteur("JK", "Rowling")
for i in range(8):
    if i >= 1:
        auteur1.ecrireUnLivre("Harry Potter " + str(i))

auteur2 = Auteur("JRR", "Tolkien")
for i in range(4):
    if i >= 1:
        auteur2.ecrireUnLivre("Le seigneur des anneaux " + str(i))

biblio1.acheterLivre(auteur1, "Harry Potter 1", 5 )
biblio1.acheterLivre(auteur1, "Harry Potter 2", 2 )
biblio1.acheterLivre(auteur1, "Harry Potter 15", 2 )
biblio1.acheterLivre(auteur2, "Harry Potter 2", 2 )
biblio1.acheterLivre(auteur2, "Le seigneur des anneaux 3", 2 )
biblio1.acheterLivre(auteur2, "Le seigneur des anneaux 2", 2 )
biblio1.acheterLivre(auteur2, "Le seigneur des anneaux 1", 2 )

print("Inventaire de départ :")
biblio1.inventaire()

biblio1.louer(client1, "Harry Potter 1")
biblio1.louer(client2, "Harry Potter 3")
biblio1.louer(client2, "Harry Potter 6")
biblio1.louer(client1, "Harry Potter 2")
biblio1.louer(client2, "Le seigneur des anneaux 3")

biblio1.rendreLivres(client1)


        




