from items import Item
import csv


class Armure(Item):
    all = []

    def __init__(self, nom, valeur: int, defense: int):
        super().__init__(nom, valeur)
        self.__defense = defense

        Armure.all.append(self)

    @property
    def defense(self):
        return self.__defense

    @defense.setter
    def defense(self, defense):
        self.__defense = defense

    @classmethod
    def create_item(cls):
        with open("armor.csv", "r") as f:
            reader = csv.DictReader(f)
            objets = list(reader)
        for objet in objets:
            Armure(
                nom=objet.get("nom"),
                valeur=int(objet.get("valeur")),
                defense=int(objet.get("defense"))
            )

    def __repr__(self):
        return f"Vous vous équipez d'une {self.nom} dont la valeur est de {self.valeur}po et qui possede une defense de {self.defense}"
