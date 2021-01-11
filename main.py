import csv
from tqdm import tqdm
from operator import itemgetter


def force_brute():
    CONST_PRIX_MAX = 500
    CONST_100 = 100
    all_action = [['share-1', 15, 10], ['share-2', 25, 15], ['share-3', 35, 20], ['share-4', 30, 17], ['share-5', 40, 25],
                  ['share-6', 11, 7], ['share-7', 13, 11], ['share-8', 24, 13], ['share-9', 17, 27], ['share-10', 21, 17],
                  ['share-11', 55, 9], ['share-12', 19, 23], ['share-13', 7, 1], ['share-14', 9, 3], ['share-15', 4, 8],
                  ['share-16', 2, 12], ['share-17', 5, 14], ['share-18', 12, 21], ['share-19', 57, 18], ['share-20', 10, 5]]
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
    print(sorted_best_action)
    test = []
    test2 = []
    for elem in sorted_best_action:
        while elem[3] > 0:
            price_500 = elem[3]
            total_benefice = elem[4]
            for action in all_action:
                price_500 += action[1]
                gain_after_2_years_by_action = (action[1] / CONST_100) * (action[2])
                total_benefice += gain_after_2_years_by_action
                test.append(action[0])
                if price_500 > CONST_PRIX_MAX:
                    price_500 = price_500 - action[1]
                    total_benefice = total_benefice-gain_after_2_years_by_action
                    del test[-1]
                if price_500 == CONST_PRIX_MAX:
                    test.append(elem[0])
                    test.append(price_500)
                    test.append(round(total_benefice, 2))
                    break
            elem[3] += - elem[1]
            gain = (elem[1]/100)*elem[2]
            elem[4] = elem[4]-gain
            if price_500 == CONST_PRIX_MAX:
                test2.append(test)
            test = []
    sorted_best_action = (sorted(test2, key=itemgetter(-1), reverse=True))
    print(sorted_best_action[0:10])




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
    print(sorted_best_action[:10])


if __name__ == "__main__":
    #opti_algo()
    force_brute()

