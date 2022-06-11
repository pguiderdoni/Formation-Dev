from items import Item
from persos import Perso
from weap import Arme
from armor import Armure
from dataclasses import dataclass
import random


def main():
    rng = list(range(10))
    Arme.create_item()
    Armure.create_item()
    lootw = random.choice(rng)
    loota = random.choice(rng)
    # creer un perso: Nom, classe, race, Or, pv
    # nom = input("Entrez votre nom")
    perso1 = Perso("Kheyla", "Guerriere", "Humaine")
    perso1.loot_arme(lootw)
    perso1.loot_armure(loota)
    print(perso1)
    perso1.show_invent_arme()
    perso1.show_invent_armure()


# print("Initialisation...")
# item1 = Item(nom="Epée", valeur=50)
# print(item1)
# print(item1.nom)
# print(item1.valeur)

if __name__ == "__main__":
    main()
