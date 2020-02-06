# 5. Запросите у пользователя значения выручки и издержек фирмы. Определите,
# с каким финансовым результатом работает фирма (прибыль — выручка больше
# издержек, или убыток — издержки больше выручки). Выведите
# соответствующее сообщение. Если фирма отработала с прибылью, вычислите
# рентабельность выручки (соотношение прибыли к выручке). Далее запросите
# численность сотрудников фирмы и определите прибыль фирмы в расчете на
# одного сотрудника.


# Выручка
revenue = int(input("Введите выручку: "))

# Издержки
costs = int(input("Введите издержки: "))

if revenue > costs:
    print("Финансовый результат: прибыль")

    # Прибыль
    profit = revenue - costs

    # Рентабельность
    profitability = profit * 100 / revenue
    print(f" Рентабельность равна: {profitability}")

    # Количество сотрудников
    peoples = int(input("Сколько человек работает в компании: "))

    # прибыль фирмы в расчете на одного сотрудника
    profit_per_employee = profit / peoples

    print(f"Прибыль в расчете на одного сотрудника равна {profit_per_employee}")
elif revenue == costs:
    print("Финансовый результат: нет дохода")
else:
    print("Финансовый результат: убыток")
