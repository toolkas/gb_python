# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие
# лекционных, практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название
# предмета и общее количество занятий по нему. Вывести словарь на экран.

# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

courses = dict()
with open("task6.file.txt", encoding="UTF-8") as f:
    for line in f.readlines():
        line = line.strip()

        course_name = line[0:line.index(":")]
        course_info = line[line.index(":"):].strip()
        course_info = "".join([x for x in course_info if x.isspace() or x.isdigit()])

        course_lessons = sum(map(int, course_info.strip().split()))
        courses[course_name] = course_lessons

print(courses)
