# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

with open('task2.file.txt', encoding='utf-8') as f:
    lines = f.readlines()

    print(f"Количество строк: {len(lines)}")

    for line in lines:
        print(f"В строке '{line.strip()}' слов: {len(line.split())}")
