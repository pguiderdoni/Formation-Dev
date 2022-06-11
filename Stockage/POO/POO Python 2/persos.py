from items import Item
from weap import Arme
from armor import Armure


class Perso:
    def __init__(self, nom: str, classe: str, race: str, thune="10", pv="100"):
        assert nom.isalpha(), "j'ai dit un nom, pas un numéro de secu!"
        self.__nom = nom
        self.__race = race
        self.__classe = classe
        self.__thune = thune
        self.__pv = pv
        self.__inventaire_arme: [Arme] = []
        self.__inventaire_armure: [Armure] = []

    @property
    def nom(self):
        return self.__nom

    @property
    def pv(self):
        return self.__pv

    @nom.setter
    def nom(self, nouv_nom):
        if nouv_nom.isalpha():
            self.__nom = nouv_nom
            print(f"Votre personnage s'appele maintenant {self.__nom}")
        else:
            print(f"Nom pourri!")

    @property
    def inventaire_arme(self):
        return self.__inventaire_arme

    @property
    def inventaire_armure(self):
        return self.__inventaire_armure

    @pv.setter
    def pv(self, nouv_pv):
        self.__pv = nouv_pv

    def show_invent_arme(self):
        for item in self.__inventaire_arme:
            print(self.__inventaire_arme)

    def show_invent_armure(self):
        for item in self.__inventaire_armure:
            print(self.__inventaire_armure)

    def loot_arme(self, item_id: int):
        if isinstance(item_id, int):
            if item_id > len(Arme.all):
                print("Cet objet n'existe pas...")
            else:
                self.__inventaire_arme.append(Arme.all[item_id])

    def loot_armure(self, item_id: int):
        if isinstance(item_id, int):
            if item_id > len(Armure.all):
                print("Cet objet n'existe pas...")
            else:
                self.__inventaire_armure.append(Armure.all[item_id])

    def __repr__(self):
        return f"{self.__nom} la {self.__classe} {self.__race} est là!\nElle a {self.__pv} points de vie\net possede {self.__thune} pieces d'or...\n"
