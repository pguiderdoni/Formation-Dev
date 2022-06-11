class Voiture:

    def __init__(self, modele: str, prix: int, vitesse: int, places: int):

        self.modele = modele
        self.prix = prix
        self.vitesse = vitesse
        self.places = places

    def change_prix(self, nouv_prix):
        self.prix = nouv_prix
        print(f"Le nouveau prix de la {self.modele} est de {self.prix}€")

    def __repr__(self):
        return f"La {self.modele} coûte {self.prix} €, a une vitesse max de: {self.vitesse}km/h, et peut accueillir {self.places} passagers."
