import csv
from tqdm import tqdm
from operator import itemgetter


def best_single_20_actions(all_action):
    CONST_PRIX_MAX = 500
    CONST_100 = 100
    list_action = []
    list_best_action = []
    for action in all_action:
        nb_action = 0
        total = 0
        while total < CONST_PRIX_MAX:
            total += action[1]
            nb_action += 1
        cout_maximum = (nb_action - 1) * action[1]
        gain_after_2_years_by_action = (action[1] / CONST_100) * (action[2])
        gain_with_500 = (nb_action - 1) * gain_after_2_years_by_action
        list_action.append(action[0])
        list_action.append(action[1])
        list_action.append(action[2])
        list_action.append(round(cout_maximum, 2))
        list_action.append(round(gain_with_500, 2))
        list_best_action.append(list_action)
        list_action = []
    sorted_best_action = (sorted(list_best_action, key=itemgetter(2), reverse=True))
    return sorted_best_action


def action_possible(action):
    CONST_PRIX_MAX = 500
    CONST_100 = 100
    list_by_action = []
    list_all_action = []
    sorted_action = (sorted(action, key=itemgetter(0), reverse=True))
    n = len(sorted_action)
    for i in range(n):
        for j in range(0, n - i - 1):
            action = [['ashare-1', 15, 10], ['bshare-2', 25, 15], ['cshare-3', 35, 20], ['dshare-4', 30, 17],
                      ['eshare-5', 40, 25], ['fshare-6', 11, 7], ['gshare-7', 13, 11], ['hshare-8', 24, 13],
                      ['ishare-9', 17, 27], ['jshare-11', 55, 9], ['kshare-12', 19, 23], ['lshare-13', 7, 1],
                      ['mshare-10', 21, 17], ['nshare-14', 9, 3], ['oshare-15', 4, 8], ['pshare-16', 2, 12],
                      ['qshare-17', 5, 14], ['rshare-18', 12, 21], ['sshare-19', 57, 18], ['tshare-20', 10, 5]]
            sorted_best_action = best_single_20_actions(action)
            if sorted_action[j] > sorted_action[j + 1]:
                sorted_action[j], sorted_action[j + 1] = sorted_action[j + 1], sorted_action[j]
                for elem in sorted_best_action:
                    while elem[3] > 0:
                        price_500 = elem[3]
                        total_benefice = elem[4]
                        for action in sorted_action:
                            price_500 += action[1]
                            gain_after_2_years_by_action = (action[1] / CONST_100) * (action[2])
                            total_benefice += gain_after_2_years_by_action
                            list_by_action.append(action[0])
                            if action == sorted_action[-1]:
                                action = sorted_action[0]
                            if price_500 > CONST_PRIX_MAX:
                                price_500 = price_500 - action[1]
                                total_benefice = total_benefice - gain_after_2_years_by_action
                                del list_by_action[-1]
                            if price_500 == CONST_PRIX_MAX:
                                list_by_action.append(elem[0])
                                list_by_action.append(price_500)
                                list_by_action.append(round(total_benefice, 2))
                                break
                        elem[3] += - elem[1]
                        gain = (elem[1] / 100) * elem[2]
                        elem[4] = elem[4] - gain
                        if price_500 == CONST_PRIX_MAX:
                            # sorted_list_by_action = (sorted(list_by_action, key=itemgetter(-1)))
                            if list_by_action not in list_all_action:
                                list_all_action.append(list_by_action)
                        list_by_action = []
    return list_all_action


def all_possibility_with_20_actions():
    action = [['ashare-1', 15, 10], ['bshare-2', 25, 15], ['cshare-3', 35, 20], ['dshare-4', 30, 17],
              ['eshare-5', 40, 25], ['fshare-6', 11, 7], ['gshare-7', 13, 11], ['hshare-8', 24, 13],
              ['ishare-9', 17, 27], ['jshare-11', 55, 9], ['kshare-12', 19, 23], ['lshare-13', 7, 1],
              ['mshare-10', 21, 17], ['nshare-14', 9, 3], ['oshare-15', 4, 8], ['pshare-16', 2, 12],
              ['qshare-17', 5, 14], ['rshare-18', 12, 21], ['sshare-19', 57, 18], ['tshare-20', 10, 5]]

    list_action1 = action_possible(action)
    sorted_all_best_action = (sorted(list_action1, key=itemgetter(-1), reverse=True))
    print(sorted_all_best_action[0:100])
    print(len(sorted_all_best_action))


def opti_algo():
    CONST_PRIX_MAX = 500
    CONST_100 = 100
    action = []
    best_action = []
    with open('dataFinance.csv', newline='') as csvfile:
        data = csv.DictReader(csvfile)
        for row in tqdm(data):
            if float(row['Cost(Euro/share)']) == 0:
                nb_action = 0
            else:
                nb_action = int(CONST_PRIX_MAX / float(row['Cost(Euro/share)']))
            cout_maximum = nb_action * float(row['Cost(Euro/share)'])
            gain_after_2_years_by_action = (float(row['Cost(Euro/share)']) / CONST_100) * (
                float(row['Profit(% post 2 years)']))
            gain_with_500 = nb_action * gain_after_2_years_by_action
            action.append(row['Shares'])
            action.append(float(row['Cost(Euro/share)']))
            action.append(float(row['Profit(% post 2 years)']))
            action.append(round(cout_maximum, 2))
            action.append(round(gain_with_500, 2))
            best_action.append(action)
            action = []
    csvfile.close()
    sorted_best_action = (sorted(best_action, key=itemgetter(4), reverse=True))
    print(sorted_best_action[0:10])


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
            all_possibility_with_20_actions()
        if choix_menu == 2:
            opti_algo()
        if choix_menu == 3:
            bool = False


if __name__ == "__main__":
    main()
