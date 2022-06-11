import csv


class Item:
    all = []

    def __init__(self, nom: str, valeur: int):
        assert len(nom) > 2, "Nom trop court!!"
        assert valeur > 0, "C'est plus !"
        self.__nom = nom
        self.__valeur = valeur
        Item.all.append(self)

    @property
    def nom(self):
        return self.__nom

    @property
    def valeur(self):
        return self.__valeur

    @nom.setter
    def nom(self, nom):
        self.__nom = nom

    @valeur.setter
    def valeur(self, valeur):
        if 0 < valeur < 1000:
            self.__valeur = valeur
        else:
            raise Exception("Ca dépasse l'entendement!")

    # Abstraction
    def __calcul_dmg(self):
        pass

    def __calcul_defense(self):
        pass

    def combat(self):
        pass



    def __repr__(self):
        return f"Ce(tte) {self.__nom} vaut {self.__valeur} pièces d'or"
