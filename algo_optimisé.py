import csv
from tqdm import tqdm
from operator import itemgetter


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
            action.append(nb_action)
            action.append(float(row['Cost(Euro/share)']))
            action.append(float(row['Profit(% post 2 years)']))
            action.append(round(cout_maximum, 2))
            action.append(round(gain_with_500, 2))
            best_action.append(action)
            action = []
    csvfile.close()
    sorted_best_action = (sorted(best_action, key=itemgetter(5), reverse=True))
    print(sorted_best_action[0:10])
    print(len(sorted_best_action))
