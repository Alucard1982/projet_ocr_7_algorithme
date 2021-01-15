from tqdm import tqdm
from operator import itemgetter


def best_single_20_actions(all_action):
    """

    fonction qui permet de calculer le meilleur investissement sur une action pour les 20 actions
    :param all_action: liste des 20 actions
    :return: une liste d'action trié du meilleure bénéfice par action au moins bon
    """
    CONST_PRIX_MAX = 500
    CONST_100 = 100
    list_action = []
    list_best_action = []
    for action in all_action:
        nb_action = int(CONST_PRIX_MAX / action[1])
        cout_maximum = nb_action * action[1]
        gain_after_2_years_by_action = (action[1] / CONST_100) * (action[2])
        gain_with_500 = nb_action * gain_after_2_years_by_action
        list_action.append(action[0])
        list_action.append(action[1])
        list_action.append(action[2])
        list_action.append(round(cout_maximum, 2))
        list_action.append(round(gain_with_500, 2))
        list_action.append(nb_action)
        list_best_action.append(list_action)
        list_action = []
    sorted_best_action = (sorted(list_best_action, key=itemgetter(2), reverse=True))
    return sorted_best_action


def action_possible(action):
    """

    fonction qui permet de trouver tte les combinaisons d'actions pour 500e pile
    :param action: une liste d'action trié du meilleure bénéfice par action au moins bon
    :return: liste de tte les combinaisons d'actions pour 500e
    """
    CONST_PRIX_MAX = 500
    CONST_100 = 100
    list_by_action = []
    list_all_action = []
    sorted_action = (sorted(action, key=itemgetter(0), reverse=True))
    n = len(sorted_action)
    for i in tqdm(range(n)):
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
                            if price_500 > CONST_PRIX_MAX:
                                price_500 = price_500 - action[1]
                                total_benefice = total_benefice - gain_after_2_years_by_action
                                del list_by_action[-1]
                            if price_500 == CONST_PRIX_MAX:
                                list_by_action.append(elem[0])
                                list_by_action.append(elem[5])
                                list_by_action.append(price_500)
                                list_by_action.append(round(total_benefice, 2))
                                break
                        elem[3] += - elem[1]
                        gain = (elem[1] / 100) * elem[2]
                        elem[4] = elem[4] - gain
                        if price_500 == CONST_PRIX_MAX:
                            if list_by_action not in list_all_action:
                                list_all_action.append(list_by_action)
                        list_by_action = []
    return list_all_action


def all_possibility_with_20_actions():
    """

    Procedure qui permet l'affichage de la meilleure combinaison d'action ainsi que la moins bonne
    Affiche aussi le nombre de combinaisons d'actions pour 500e pile
    """
    action = [['ashare-1', 15, 10], ['bshare-2', 25, 15], ['cshare-3', 35, 20], ['dshare-4', 30, 17],
              ['eshare-5', 40, 25], ['fshare-6', 11, 7], ['gshare-7', 13, 11], ['hshare-8', 24, 13],
              ['ishare-9', 17, 27], ['jshare-11', 55, 9], ['kshare-12', 19, 23], ['lshare-13', 7, 1],
              ['mshare-10', 21, 17], ['nshare-14', 9, 3], ['oshare-15', 4, 8], ['pshare-16', 2, 12],
              ['qshare-17', 5, 14], ['rshare-18', 12, 21], ['sshare-19', 57, 18], ['tshare-20', 10, 5]]

    list_action1 = action_possible(action)
    sorted_all_best_action = (sorted(list_action1, key=itemgetter(-1), reverse=True))
    print(sorted_all_best_action[0])
    print(sorted_all_best_action[-1])
    print(len(sorted_all_best_action))
