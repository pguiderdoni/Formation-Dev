from cars import Voiture


class User:
    nationalite = "Corse"

    def __init__(self, first_name: str, last_name: str, argent: float, age: int, droits="utilisateur"):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.argent = argent
        self.droits = droits
        self.voitures = []
        print(f"Bienvenue {self.first_name}{self.last_name}, vous avez {self.age} ans et vous êtes {droits}!")

    def ajout_voiture(self, new_car: Voiture):
        if isinstance(new_car, Voiture):
            self.voitures.append(new_car)
        else:
            print("On a dit un voiture connard...")

    def voir_voitures(self):
        print("Voici vos voitures")
        for voiture in self.voitures:
            print(f"- {voiture}")

    def verif_droits(self):
        if self.droits == "administrateur":
            return True
        else:
            return False

    def modifier_age(self, new_age: int):
        self.age = new_age

    @staticmethod
    def a_bcp_argent(montant: float):
        if montant > 100_000:
            print("Vous votez Macron")
        else:
            print("Melenchon...")

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.first_name} {self.last_name} {self.droits}"
