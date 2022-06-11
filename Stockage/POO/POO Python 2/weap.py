from items import Item
import csv


class Arme(Item):
    all = []

    def __init__(self, nom, valeur: int, degats: int):
        super().__init__(nom, valeur)
        self.__degats = degats

        Arme.all.append(self)

    @property
    def degats(self):
        return self.__degats

    @degats.setter
    def degats(self, degats):
        self.__degats = degats

    @classmethod
    def create_item(cls):
        with open("weap.csv", "r") as f:
            reader = csv.DictReader(f)
            objets = list(reader)
        for objet in objets:
            Arme(
                nom=objet.get("nom"),
                valeur=int(objet.get("valeur")),
                degats=int(objet.get("degats"))
            )

    def __repr__(self):
        return f"Vous trouvez un(e) {self.nom} dont la valeur est de {self.valeur}po et qui fait {self.degats} points de degats"
