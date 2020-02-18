# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные
# аргументы. Реализовать вывод данных о пользователе одной строкой.


def print_person_info(name, last_name, birth_year, city, email, phone):
    print(f"{last_name} {name}, {birth_year} года рождения, проживает в {city}. Email: {email}, Номер телефона: {phone}")


person_name = input("Введите имя: ").strip()
person_last_name = input("Введите фамилию: ").strip()
person_birth_year = int(input("Введите год рождения: ").strip())
person_city = input("Введите город проживания: ").strip()
person_email = input("Введите email: ").strip()
person_phone = input("Введите телефон: ").strip()

print_person_info(
    name=person_name,
    last_name=person_last_name,
    birth_year=person_birth_year,
    city=person_city,
    email=person_email,
    phone=person_phone
)
