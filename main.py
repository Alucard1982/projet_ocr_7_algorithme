import algo_optimisé
import algo_force_brute

def menu():
    print("Bienvenu dans le menu des actions")
    print("1-Algo Force Brute pour 20 actions")
    print("2-Algo opti pour 100000 actions")
    print("3-Quitter le menu")


def saisie_int(message):
    """

    Méthode qui permet de verouiller les saisies int
    :param message: le message écrit
    :return: la saisie en int
    """
    try:
        return int(input(message))
    except ValueError:
        print("attention ce n'est pas un chiffre ")
        return saisie_int(message)


def main():
    bool = True
    while bool == True:
        menu()
        choix_menu = saisie_int(" Choisissez une action : --> ")
        if choix_menu == 1:
            algo_force_brute.all_possibility_with_20_actions()
        if choix_menu == 2:
            algo_optimisé.opti_algo()
        if choix_menu == 3:
            bool = False


if __name__ == "__main__":
    main()



