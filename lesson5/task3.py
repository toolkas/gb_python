# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

with open('task3.file.txt', encoding='utf-8') as f:
    salary_sum = 0
    count = 0

    for line in f.readlines():
        last_name, salary = (line.strip().split())
        salary = float(salary)

        if salary < 20000:
            print(f"{last_name} получает менее 20 тыс. рублей")
        salary_sum += salary
        count += 1

    print(f"Средний доход сотрудника равен {salary_sum / count} рублей")
