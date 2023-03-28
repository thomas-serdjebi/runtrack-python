from job0 import Personne

class Livre:
    def __init__(self, titre, auteur):
        self._titre = titre
        self._auteur = auteur

        
    def get_titre(self):
        return self._titre

    def get_auteur(self):
        return self._auteur
    
    def set_titre(self, titre):
        self._titre = titre

    def set_auteur(self, auteur):
        self._auteur = auteur

    def print(self):
        print(self._titre)

class Auteur(Personne):
    def __init__(self, nom, prenom):
        super().__init__(nom, prenom)
        self._oeuvre = []

    def get_oeuvre(self):
        return self._oeuvre

    def set_oeuvre(self, oeuvre):
        self._oeuvre = oeuvre
    
    def listerOeuvre(self):
        for livre in self._oeuvre:
            print(livre.get_titre())
    
    def ecrireUnLivre(self, titre):
        livre = Livre(titre, self)
        self._oeuvre.append(livre)


    
    
