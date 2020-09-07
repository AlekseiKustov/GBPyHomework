#1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.


some_list = ['program', 1, 1.5, True, "1"]
print("Количество элеметов в списке: ",len(some_list))
#print(type(some_list[0:]))
#print(type(some_list[0]))
##print(type(some_list[1]))
##print(type(some_list[2]))
##print(type(some_list[3]))
##print(type(some_list))
some_list.append(22)
for i in some_list:
    print(f'{i}', 'Тип элемента: ', type(i))
# Принт по индексу элемента выдаёт верный тип элемента (строка 10-13), но Принт среза элементов выдаёт тип list(строка 9). Почему?




#2. Для списка реализовать обмен значений соседних элементов,
#т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().


list = []# заводим пустой список
for i in range(int(input("Введите количество элементов в списке: "))):# задаём количество элемент в списке
    list.append(int(input("Введите элементы списка: "))) # вводим элементы списка
print(list) # получаем список
def swap_digits(array): # Объявляем новую функцию
    swapped_result = [
        x
        for pair in zip(array[::2], array[1::2])
        for x in reversed(pair)
    ]
    if len(array) % 2 != 0:
        swapped_result.append(array[-1])
    return swapped_result

print(swap_digits(list))


#3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.


#list
month = int(input("Введите № месяца: "))
season_name = ['Зима', 'Весна', 'Лето', 'Осень']


if 2 < month < 6:
   print(f'{month} месяц - ', season_name[1])
elif 5 < month < 9:
    print(f'{month} месяц - ', season_name[2])
elif 8 < month < 12:
    print(f'{month} месяц - ', season_name[3])
else:
    print(f'{month} месяц - ', season_name[0])

#dict
seasons = {'Зима': [1, 2, 12], 'Весна': [3, 4, 5], 'Лето': [6, 7, 8], 'Осень': [9, 10, 11]}
season_number = int(input('Выберите № месяца: '))
for seasons, month_number in seasons.items():
    if season_number in month_number:
        print(f'{season_number} -  {seasons}')


#4Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

string = input("Введите слова через пробел: ")
string = string.split(<3)
line = 1
for string_word in string:
    print('{}: {:}'. format(line, string_word[:10]))
    line += 1

#5Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
#Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
#Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
#Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
#Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
#Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].


my_list = [7, 5, 3, 3, 2]
new_elements = int(input())
for i in range(new_elements):
    new_element = int(input())
    my_list.append(new_element)
my_list.sort(reverse=True)
print(my_list)


#Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
#Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
#Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
#Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
#Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
#Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].


goods = []
exit_from_loop = 'Waiting...'
x = 1
while exit_from_loop != "N":
    name = input('Введите наименование товара: ')
    price = int(input('Введите цену товара: '))
    amount = int(input('Введите  количество товаров: '))
    unit = input('Введите еденицу измерения количества товара: ')

    goods_tuple = (x, {'Наименование товара': name, 'Цена': price, 'Количество товаров': amount, 'Еденицы': unit})
    goods.append(goods_tuple)
    exit_from_loop = input('Для прекращения нажмите "N", для продолжения всё остальное: ')
    exit_from_loop = exit_from_loop.upper()
    x += 1

name_list =[]
price_list =[]
amount_list =[]
unit_list =[]

for product in goods:
    name_list.append(product[1].get('Наименование товара'))
    price_list.append(product[1].get('Цена'))
    amount_list.append(product[1].get('Количество товаров'))
    unit_list.append(product[1].get('Еденицы'))

name_list = list(set(name_list))
price_list = list(set(price_list))
amount_list = list(set(amount_list))
unit_list = list(set(unit_list))

evolution_dict = {'Наименование товара': name_list, 'Цена': price_list, 'Количество товаров': amount_list, 'Еденицы': unit_list}

print(evolution_dict)

