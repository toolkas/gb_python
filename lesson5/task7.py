# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
#
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
#
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.

import json

with open('task7.file.txt', encoding="utf-8") as f:
    total_profit = 0
    firms_info = dict()
    for line in f.readlines():
        (name, form, revenue, costs) = line.strip().split()
        profit = float(revenue) - float(costs)
        if profit > 0:
            total_profit += profit

        firms_info[name] = profit
    avg_profit = total_profit/len(firms_info)

    firm_list = [firms_info, {"average_profit": avg_profit}]
    with open('task7.out.js', "w", encoding="utf-8") as out:
        json.dump(firm_list, out)
