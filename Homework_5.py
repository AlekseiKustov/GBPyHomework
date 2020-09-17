#1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.




with open('C:/Users/Алексей/Desktop/PyProjects/beginning/textX.txt', 'x') as file:
    while True:
        user_print = input('Введите строку: ')
        if user_print == '':
            break
        file.write(user_print + '\n')


#2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.
count = 0
with open ('C:/Users/Алексей/Desktop/PyProjects/beginning/text2.txt') as file:
    for i, line in enumerate(file, 1):
        print(f'В {i} строке {len(line)} символов')
        count += 1
    print('Количество строк в файле: ', count)


#3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

with open('C:/Users/Алексей/Desktop/PyProjects/beginning/text3salary.txt') as file:
    salary_sum = 0
    count = 0
    for line in file:
        name, salary = line.split()
        salary = int(salary)
        salary_sum += salary
        count += 1
        if salary < 20000:
            print(name, salary)
    print('Средняя зарплата: ', salary_sum / count)

#4. Создать (не программно) текстовый файл со следующим содержимым:
#One — 1
#Two — 2
#Three — 3
#Four — 4
#Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.


numbers = {'One': 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
with open('C:/Users/Алексей/Desktop/PyProjects/beginning/text4.txt') as file, open('C:/Users/Алексей/Desktop/PyProjects/beginning/text4rus.txt', 'w') as rus_file:
    lines_from_file = [line.split() for line in file]
    rus_lines = [[numbers[el[0]], el[1], el[2]] for el in lines_from_file]
    for el in rus_lines:
        rus_file.writelines(' '.join(el) + '\n')


#5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.



with open('C:/Users/Алексей/Desktop/PyProjects/beginning/text5X.txt', 'x') as file:
    line = input('Введите цифры через пробел \n')
    my_numb = line.split()
    print(sum(map(int, my_numb)))


#6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет
# и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.
#Примеры строк файла:
#Информатика: 100(л) 50(пр) 20(лаб).
#Физика: 30(л) — 10(лаб)
#Физкультура: — 30(пр) —
#Пример словаря:
#{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

with open('C:/Users/Алексей/Desktop/PyProjects/beginning/text6.txt') as file:
    file_dict = {}
    for line in file:
        hourse = line.split()
        for i in range(1, 4):
            if hourse[i] != "—":
                hourse[i] = int(hourse[i].rstrip('(лпраб'))
            else:
                hourse[i] = 0
        courses_dict[hourse[0].rstrip(':')] = sum(hourse[1:])
    print(courses_dict)


#7. Создать (не программно) текстовый файл,
# в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
#Пример строки файла: firm_1 ООО 10000 5000.
#Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
#Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
#Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#Итоговый список сохранить в виде json-объекта в соответствующий файл.
#Пример json-объекта:
#[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#Подсказка: использовать менеджеры контекста.


import json
with open('C:/Users/Алексей/Desktop/PyProjects/beginning/text7.txt') as file, open('C:/Users/Алексей/Desktop/PyProjects/beginning/text7_1.json') as file_1:
    firm_dict = {}
    count = 0
    average_profit = 0
    for line in file:
        firm_list = line.split()
        profit = int(firm_list[2]) - int(firm_list[3])
        firm_dict[firm_list[0]] = profit
        if profit > 0:
            average_profit += profit
            count += 1
    average_profit /= count
    result_list = [firm_dict, {'average_profit': average_profit}]
    print(result_list)
    json.dump(result_list, file_1)