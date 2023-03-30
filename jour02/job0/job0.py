class Personne:
    def __init__(self, nom, prenom):
        self._nom = nom
        self._prenom = prenom
    
    def SePresenter(self):
        print(self._nom + " " + self._prenom)
    
    def get_nom(self):
        return self._nom

    def get_prenom(self):
        return self._prenom
    
    def set_nom(self, nom):
        self._nom = nom

    def set_prenom(self, prenom):
        self._prenom = prenom

personne1 = Personne("Thomas", "Serdjebi")
personne2 = Personne("Paul", "Serdjebi")
personne3 = Personne("Richard", "Serdjebi")
personne4 = Personne("Karim", "Serdjebi")

personne1.SePresenter()
personne2.SePresenter()
personne3.SePresenter()
personne4.SePresenter()

    