from user import User
from cars import Voiture


def main():
    machin = User("Kurosawa", "-San", 1000, 40,  "administrateur")
    voiture1 = Voiture("Tesla", 45_000, 280, 5)
    voiture2 = Voiture("TurboCrado", 3_500, 134, 4)
    voiture3 = Voiture("Fiesta ST", 30_000, 242, 5)


    machin.verif_droits()
    if machin.verif_droits:
        machin.ajout_voiture(voiture1)
        machin.ajout_voiture(voiture2)
        machin.ajout_voiture(voiture3)
        machin.voir_voitures()
        voiture1.change_prix(23500)

    else:
        print("Vous n'avez pas les droits d'accès")


if __name__ == "__main__":
    main()
