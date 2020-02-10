# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к
# какому времени года относится месяц (зима, весна, лето, осень). Напишите решения
# через list и через dict.

month = int(input("Введите номер месяца (от 1 до 12): "))

# Решение задачи через dict
season_by_month = {
    1: "зима",
    2: "зима",
    3: "весна",
    4: "весна",
    5: "весна",
    6: "лето",
    7: "лето",
    8: "лето",
    9: "осень",
    10: "осень",
    11: "осень",
    12: "зима",
}

print(f"Месяц {month} относится к времени года: {season_by_month[month]}")

# Решение задачи через list
season_by_month2 = [
    "зима",
    "зима",
    "весна",
    "весна",
    "весна",
    "лето",
    "лето",
    "лето",
    "осень",
    "осень",
    "осень",
    "зима",
]


print(f"Месяц {month} относится к времени года: {season_by_month2[month]}")
