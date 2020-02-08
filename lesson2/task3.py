# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к
# какому времени года относится месяц (зима, весна, лето, осень). Напишите решения
# через list и через dict.

month = int(input("Введите номер месяца (от 1 до 12): "))

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

season = season_by_month[month]
print(f"Месяц {month} относится к времени года: {season}")

months_and_seasons = [
    {"month": 1, "season": "зима"},
    {"month": 2, "season": "зима"},
    {"month": 3, "season": "весна"},
    {"month": 4, "season": "весна"},
    {"month": 5, "season": "весна"},
    {"month": 6, "season": "лето"},
    {"month": 7, "season": "лето"},
    {"month": 8, "season": "лето"},
    {"month": 9, "season": "осень"},
    {"month": 10, "season": "осень"},
    {"month": 11, "season": "осень"},
    {"month": 12, "season": "зима"}
]

season2 = ""
for item in months_and_seasons:
    if item["month"] == month:
        season2 = item["season"]
        break

print(f"Месяц {month} относится к времени года: {season2}")
