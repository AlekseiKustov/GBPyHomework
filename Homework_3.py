#1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def my_dev(arg_1, arg_2):
    return arg_1 / arg_2
arg_1 = int(input('First argument: '))
arg_2 = int(input('Second argument: '))
while arg_2 == 0:
    print('You tap on ZERO, try another argument')
    break
print(my_dev(arg_1, arg_2))

#2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def database(name, surname, year, city, email, telephone):
    print(name, surname, year, city, email, telephone)
database(name ='Bob', surname ='Silent', year = '1984', city = 'Boston', email = 'backkick@gmail.com', telephone = '00734')
#user_name = input('Yor name:')
#user_surname = input('Your surname: ')
#user_birth_year = input('Your birthday year: ')
#user_city = input('Your city: ')
#user_email = input('Your email: ')
#user_phone = int(input('Your phone: '))


#print(database(f"'{user_name}", f"{user_surname}", f"{user_birth_year}", f"{user_city}", f"{user_email}", f"{user_phone}'" ))


#3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.


def my_func(*args):
   arguments = sorted(args)
   two_max_arguments = arguments[-2:]
   return two_max_arguments[0] + two_max_arguments[1]
print(my_func(1, 220, 100, 101, 66))


# 4 Программа принимает действительное положительное число x
# и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.


def my_func_1(x, y):
    return x ** y


def my_func_2(x, y):
    z = 1
    for i in range(abs(y)):
       z = z * x
    return 1 / z


x_num = float(input('X argument: '))
y_num = int(input('Y argument: '))

print(my_func_1(x_num, y_num))
print(my_func_2(x_num, y_num))



#5 Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

def sum_num():
    result = 0
    while True:
        user_numbers = input('Введите число через пробел. Для выхода нажмите"!": ')
        for number in user_numbers.split(' '):
            if number == '!':
                return result
            result += int(number)
        print('Текущая сумма: ', result)

    return result
sum_max = sum_num()
print(sum_max)


#6Реализовать функцию int_func(), принимающую слово из маленьких латинских букв
# и возвращающую его же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
#Продолжить работу над заданием.
# В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().



def int_func(string_text):
    text_list = string_text.split(' ')
    new_text_list = []
    for word in text_list:
        new_text_list.append(word.capitalize())
    return ' '.join(new_text_list)
user_string = input('Вводите слова с маленькой буквы разделяя пробелом: ')
print(int_func(user_string))