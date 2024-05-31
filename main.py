import re
import os
from colorama import Fore, Back, Style
import time
import shutil

'''Тема словари - 2,3,4,5 .
Множество - Таблица рекордов,
День решения задач - с 5 задания по 11 задание ,
Функции практика с 2 по 5
Тема sort - Задача «Каталог книг»,
Lambda - с 4 до 8 ,
Re первая часть 5 задание ,
Re с 2 по 4 , Тема OS 4-6 задание'''




#Практика

'''
1) Запустите код примера со слайда Русско-английский словарь. Как видите, словарь
отсортирован по ключам, т.е. пары в словаре идут в порядке возрастания по русскому
алфавиту. Вот такое дополнение позволит отсортировать словарь по значениям (т.е. по
англ. алфавиту в значениях):
sorted_values = sorted(rusEng.values()) # отсортированный список значений
engRus = {} # пустой будущий англо-русский словарь
# в цикле пройти все значения (англ.слова); на каждом шаге находить
соответствующее данному значению русское слово в ключах и помещать его в
качестве ключа в пару к данному значению
for i in sorted_values:
for k in rusEng.keys():
if rusEng[k] == i:
engRus[k] = rusEng[k]
break
print(engRus) # вывод на экран получившегося словаря
Дополните код таким образом, чтобы на выходе получался именно англо-русский
словарь, т.е. поменяйте местами ключи и значения в словаре engRus.'''

#Дополнительная практика

'''2) Составьте программу-оболочку для словаря со следующим функционалом:
1. Вывести английский перевод по введённому русскому слову;

2. Вывести русский перевод по введённому английскому слову;

3. Добавить слово и его перевод в словарь.
Для каждого действия, если оно невозможно, должно быть предусмотрено
сообщение об ошибке.

3) Напишите генератор словаря, который будет получать на вход строку из
маленьких английских букв и записывать в качестве ключа букву, а в качестве
значения – количество этих букв в исходной строке.
Пример
Вход: abadfdsfasb
Выход: {'a': 3, 'b': 2, 'd': 2, 'f': 2, 's': 2}

4. Определить количество повторов слов во входной строке.
Ввод: строка текста, в которой слова разделяются строго одним
пробелом.
Вывод: строки, каждая из которых состоит из слова и количества
повторений для каждого из них. Строки должны быть отсортированы по
убыванию встречаемости.
Пример ввода:
миллион миллион миллион алых роз
Пример вывода:
миллион 3
алых 1'''

#Задание на генераторы словарей

'''5. На вход программе подаются результаты
судейства по фигурному катанию. В первой
строке N - количество участников и S -
количество судей, разделённые пробелом,
во второй - фамилии спортсменов через
запятую с пробелом, в последующих N
строках – S оценок судей в виде числа с
плавающей точкой от 0.0 до 6.0.
На экран нужно вывести фамилии
спортсменов, занявших по итогу
соревнований 1, 2 и 3 места, и их средний
балл. Дроби округлить до второго знака
после запятой.
12

Пример ввода
4 3
Асланова Иванова Петренко Ким
5.5 5.8 4.9
5.2 5.3 5.2
6.0 6.0 6.0
5.4 5.3 5.1
Пример вывода
Петренко 6.00
Асланова 5.40
Ким 5.27'''



"""rusEng = {
    'автомобиль': 'car',
    'дом': 'house',
    'кошка': 'cat',
    'собака': 'dog'
}

sorted_values = sorted(rusEng.values())
engRus = {}
for i in sorted_values:
    for k in rusEng.keys():
        if rusEng[k] == i:
            engRus[k] = rusEng[k]
            break

def translation_rus(words):
    '''Перевода русского слова по английскому'''
    if words in engRus.keys():
        return engRus[words]
    else:
        return 'Такого слова нет в словаре'

def translation_eng(words):
    '''Перевода английского слова по русскому'''
    if words in engRus.values():
        return list(engRus.keys())[list(engRus.values()).index(words)]
    else:
        return 'Такого слова нет в словаре'

def add_word(russian, english):
    ''''Добавляем слова и его перевода в словарь'''
    if russian in rusEng:
        return 'Слово уже существует в словаре.'
    else:
        rusEng[russian] = english
        return 'Слово успешно добавлено в словарь.'

while True:
    print('Выберите действие:')
    print('1. Вывести английский перевод по русскому слову')
    print('2. Вывести русский перевод по английскому слову')
    print('3. Добавить слово и его перевод в словарь')
    print('4. Выйти из программы')

    choice = input('Введите ваш выбор: ')

    if choice == '1':
        words = input('Введите Русское слово: ')
        print(translation_rus(words))
    elif choice == '2':
        words = input('Введите Английское слово: ')
        print(translation_eng(words))
    elif choice == '3':
        russian_word = input('Введите руское слово: ')
        english_word = input('Введите английское слово: ')
        print(add_word(russian_word, english_word))
    elif choice == '4':
        print('Программа завершена.')
        break
    else:
        print("Неверный выбор. Пожалуйста, выберите от 1 до 4.")"""


#ГЕНЕРАТОР СЛОВАРЯ


"""def generate_dict(input_1):
    char_dict = {}
    for char in input_1:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

input_1 = input("Введите строку из маленьких английских букв: ")
result_dict = generate_dict(input_1)
print(result_dict)"""


#СЧИТАТЬ СЛОВА В СТРОКЕ


"""def count_word(input_1):
    '''Считать слова в строке'''
    word_dict = {}
    words = input_1.split()
    for word in words:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    sorted_dict = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)
    return sorted_dict

input_1 = input("Введите строку текста: ")
result = count_word(input_1)

for word, count in result:
    print(f"{word} {count}")"""


#ЗАДАНИЕ  5


"""def calculate_average(scores):
    return round(sum(scores) / len(scores), 2)

# Ввод количества участников и судей
n, s = map(int, input("Введите количество участников и количество судей, разделенные пробелом: ").split())

# Ввод фамилий участников
participants = input("Введите фамилии участников через запятую и пробел: ").split(", ")

# Ввод оценок судей для каждого участника
print("Введите оценки судей для каждого участника:")
judges_scores = []
for participant in participants:
    print(f"Оценки для участника {participant}:")
    scores = list(map(float, input().split()))
    judges_scores.append(scores)

# Вычисляем средний балл для каждого участника
average_scores = {}
for participant, scores in zip(participants, judges_scores):
    average_scores[participant] = calculate_average(scores)

# Сортируем участников по среднему баллу
sorted_participants = sorted(average_scores.items(), key=lambda x: x[1], reverse=True)

# Выводим результаты
for participant, average_score in sorted_participants[:3]:
    print(f"{participant} {average_score:.2f}")"""


#МНОЖЕСТВА


'''Требуется вывести таблицу
рекордов – троих лучших
игроков. Для каждого игрока
учитывается только один его
результат – самый лучший:
1. D 3001
2. A 691
3. C 435
 Программа получает на вход
перечень результатов игр в
некоторую игру в следующем виде:
6
A 675
B 249
C 435
A 675
A 691
D 3001'''


"""results = {}
# Обработка входных данных
n = int(input("Введите количество результатов игр: "))
for i in range(n):
    line = input().split()
    if len(line) != 2:
        print("Неверный формат строки. Используйте формат 'Игрок Результат'.")
        continue
    player, score = line
    try:
        score = int(score)
    except ValueError:
        print(f"Ошибка: '{score}' не является корректным числом. Пропуск строки.")
        continue
    # Обновление лучшего результата игрока
    if player not in results or score > results[player]:
        results[player] = score
# Сортировка по убыванию результатов и вывод трех лучших результатов
sorted_results = sorted(results.items(), key=lambda x: x[1], reverse=True)
print("Таблица рекордов – троих лучших игроков:")
for i, (player, score) in enumerate(sorted_results[:3], start=1):
    print(f"{i}. {player} {score}")"""


#ДЕНЬ РЕШЕНИЯ ЗАДАЧ 5 - 11

"""# 5.Напишите программу, которая принимает два списка и выводит все элементы первого, которых нет во втором.


list_1 = [1,3,2,5,6,7]
list_2 = [2,4,6]
def lists(list_1,list_2):
    elements = [element for element in list_1 if element not in list_2]
    return elements
result = lists(list_1,list_2)
print(result)


# 6.Посчитайте, сколько раз символ встречается в строке.


print('введите строку:')
user_string = input()
print('символ встречается в строке:')
symbol = input()
counter = user_string.count(symbol)
print(counter)
print(f"Символ '{symbol}' встречается в строке '{user_string}' {counter} раз(а)")


#7.Напишите проверку на то, является ли строка палиндромом. Палиндром — это слово или фраза, которые одинаково читаются слева направо и справа налево.


word = input("Введите слово: ")
def palindrome(word):
    word = word.lower()
    if word == word[::-1]:
        return True
    else:
        return False
if palindrome(word):
    print('Да, это палиндром')
else:
    print('Нет, это не палиндром')


#8.Напишите программу для слияния нескольких словарей в один


dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict1.update(dict2)
print('Соедененный словарь: ', dict1)


#9.Даны списки: Нужно вернуть список, который состоит из элементов, общих для этих двух списков.


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
set_a = set(a)
set_b = set(b)
common_a_b = list(set_a.intersection(set_b))
print('Общие элементы: ', common_a_b)


#10.Программа «Опрос»


Список вопросов
questions = [
    '1. Чем отличается список от множества?',
    '2. Какие типы данных в Python относятся к неизменяемым?',
    '3. Какой тип данных имеет k?\nk = (3, 6, 7, -10)',
    '4. Как убрать из списка [4,4,5,5,6,6] повторяющиеся элементы? Предложите два правильных ответа.',
    '5. Какой режим открытия файла предпочтительно использовать, если файл часто открывается в течение работы программы и туда заносятся мелкие изменения?'
]
                #список вопросов

answers = [
    ('Список - упорядоченная коллекция, множество - неупорядоченная коллекция',
     'Список может содержать дубликаты, множество - нет'),
    ('Кортежи, строки', 'Списки, множества'),
    ('Кортеж', 'Список', 'Множество'),
    ('Преобразовать в множество и обратно в список', 'Использовать функцию set() для удаления дубликатов',
     'Использовать цикл и проверять каждый элемент на наличие в списке'),
    ('"a+"', '"r+"', '"w"')
]
                #варианты ответов

correct_answers = 0

for question, options in zip(questions, answers):
    print(question)
                # проход по вопросам и вывод их

    for i, option in enumerate(options):
        print(f'{i + 1}. {option}')
                # вывод вариантов ответов

    user_answer = input('Введите номер правильного ответа: ')
    if user_answer.isdigit() and 1 <= int(user_answer) <= len(options):
        if options[int(user_answer) - 1] == options[0]:
            correct_answers += 1
                # проверяем ответ пользователя

print(f'Вы ответили правильно на {correct_answers} из {len(questions)} вопросов.')


# 11.Чат


chat = 'chat.txt'
user_data = 'userdata.txt'

def read_chat():
    '''функция  для чтения файла чата.'''
    
    with open(chat, 'r', encoding='utf-8') as file:
        print(file.read())

def message(username, message):
    '''функция для записи сообщения в чат.'''
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
                # настоящее время

    with open(chat, 'a', encoding='utf-8') as file:
        file.write('\n{} ({})\n{}\n'.format(username, timestamp, message))
        # открываем файл чата и записываем сообщение с реальной временной меткой

def authenticate():
    
    '''функция проверяет логин и пароль пользователя.'''
    
    username = input('Введите логин: ').lower()
    password = input('Введите пароль: ').lower()

    with open(user_data, 'r', encoding='utf-8') as file:
        for line in file:
            stored_username, stored_password = line.strip().split(':')
            # читаем информацию о пользователях и проверяем

            if stored_username.lower() == username and stored_password == password:
                return True
            # проверяем логин и пароль с данными из файла

    print('Ошибка: Неверный логин или пароль.')
    return False

def main():
    '''Основная функция для запуска чата.'''

    if not authenticate():
        return
                # проверяем аутентификацию

    read_chat()
    username = input('Введите ваше имя: ')
    user_message = input('Введите ваше сообщение: ')
    message(username, user_message)
    print('Сообщение отправлено.')"""


#КАТАЛОГ КНИГ


'''База данных книг books.txt выглядит так: каждая строка базы – одна
книга. Есть 4 графы: Автор, название, год издания, цена. Графы
разделяются символом $. Маркер конца строки #.
1. Отсортируйте книги по дате издания и сохраните это в новом файле.
2. Выведите в консоль новинки 2022 года в порядке убывания цены.'''



##pattern = r'^(.*?)\$(.*?)\$(.*?)\$(.*?)#$'
# Регулярное выражение для разбора каждой строки

"""with open("books.txt", "r") as file:
    '''Открываем файл и читаем'''
    books = file.readlines()

sorted_books = []


for line in books:
    '''Извлекаем информацию с помощью регулярного выражения'''
    match = re.match(pattern, line.strip())
    if match:
        author, title, year, price = match.groups()
        sorted_books.append((author, title, int(year), int(price)))

# Сортируем книги по году (по возрастанию) и цене (по убыванию)
sorted_books = sorted(sorted_books, key=lambda x: (x[2], -x[3]))


with open("sorted_books.txt", "w") as file:
    '''Записываем отсортированные книги'''
    for book in sorted_books:
        file.write(f"{book[0]}${book[1]}${book[2]}${book[3]}#\n")

# Выводим новые издания 2022 года в порядке убывания цен
print("Новые издания 2022 года в порядке убывания цены:")
for book in sorted_books:
    if book[2] == 2022:
        print(f"{book[1]} ({book[0]}): {book[3]} руб.")"""



# Lambda - с 1 до 8

'''1)Преобразование элементов списка: Используйте lambda-функцию для умножения
каждого элемента списка на 2.'''


"""numbers = [1, 2, 3, 4, 5]

# Применение lambda-функции
numbers_x2 = list(map(lambda x: x * 2, numbers))

# Вывод результата
print(numbers_x2)"""

'''Калькулятор с lambda-функциями: Создайте простой калькулятор, используя
lambda-функции для выполнения основных математических операций (сложение,
вычитание, умножение, деление).'''



"""# Определение lambda-функций для основных математических операций
addition = lambda x, y: x + y
subtraction = lambda x, y: x - y
multiplication = lambda x, y: x * y
division = lambda x, y: x / y if y != 0 else 'Error: Деление на ноль'

# Функция калькулятора
def calculator(x, y, operation):
    return operation(x, y)

while True:
    # Ввод операции от пользователя
    operation = input("Выберите операцию (+, -, *, /) или 'exit' для выхода: ").strip()

    if operation == 'exit':
        print("Выход из калькулятора.")
        break

    # Проверка на корректность введенной операции
    if operation not in ('+', '-', '*', '/'):
        print("Некорректная операция. Попробуйте снова.")
        continue

    try:
        # Ввод чисел от пользователя
        num1 = float(input("Введите первое число: ").strip())
        num2 = float(input("Введите второе число: ").strip())
    except ValueError:
        print("Некорректный ввод. Пожалуйста, введите числа.")
        continue

    # Выбор соответствующей операции
    if operation == '+':
        result = calculator(num1, num2, addition)
    elif operation == '-':
        result = calculator(num1, num2, subtraction)
    elif operation == '*':
        result = calculator(num1, num2, multiplication)
    elif operation == '/':
        result = calculator(num1, num2, division)

    print(f"Результат: {result}")"""

'''data = [['2001638940179228', 3922280], ['4578638940179227', 1778600],
['2001557163484689', 4035370]]
Напишите lambda-функцию, которая преобразует вторые значения в каждом
вложенном списке следующего списка данных в строковый тип данных'''


"""# Исходный список данных
data = [['2001638940179228', 3922280], ['4578638940179227', 1778600], ['2001557163484689', 4035370]]

# Преобразование вторых значений в строковый тип данных
transformed_data = list(map(lambda x: [x[0], str(x[1])], data))

print(transformed_data)"""




'''Файл clients.txt организован как
НомерКартыКлиента Сумма Входящего Перевода
Номер карты каждого клиента содержит 16 цифр, первые 4 из которых –
код банка.

Из списка банковских переводов clients.txt узнайте, сколько всего разных
клиентов получали переводы (Ответ: 418).

В списке банковских переводов clients.txt найдите клиента, который
переводил средства чаще других. Выведите на экран номер его карты в
международном стандартном виде – каждые 4 цифры разделяются
пробелами.

Выведите на экран номер карты, на которую поступил самый маленький
перевод, а также величину этого перевода.

Выведите на экран название банка, в который поступило наибольшее
количество переводов

Выведите на экран список названий банков, отсортированный по
общему объёму поступивших переводов'''


"""# Чтение данных из файлов с проверкой ошибок
try:
    with open("clients.txt", "r") as file:
        clients_data = file.readlines()
except FileNotFoundError:
    print("Файл 'clients.txt' не найден.")
    clients_data = []

try:
    with open("banks.txt", "r") as file:
        banks_data = file.readlines()
except FileNotFoundError:
    print("Файл 'banks.txt' не найден.")
    banks_data = []

# Словарь для хранения общего объема переводов по каждому банку
bank_transfers = {}
bank_names = {}

# Проверка данных о банках и создание словаря названий банков
for line in banks_data:
    parts = line.strip().split(maxsplit=1)
    if len(parts) < 2:
        continue
    bank_code = parts[0]
    bank_name = parts[1].strip()
    bank_names[bank_code] = bank_name
    bank_transfers[bank_code] = 0

# Проверка данных о клиентах и подсчет общего объема переводов для каждого банка
for line in clients_data:
    parts = line.strip().split()
    if len(parts) < 2:
        continue
    bank_code = parts[0][:4]
    try:
        transfer_amount = int(parts[1])
    except ValueError:
        print(f"Неверный формат суммы перевода: {parts[1]}")
        continue
    if bank_code in bank_transfers:
        bank_transfers[bank_code] += transfer_amount
    else:
        # Если код банка отсутствует в списке, добавим его с соответствующим переводом
        bank_transfers[bank_code] = transfer_amount
        bank_names[bank_code] = f"Unknown Bank {bank_code}"

# Сортировка банков по объему переводов
sorted_banks = sorted(bank_transfers.items(), key=lambda x: x[1], reverse=True)

# Вывод результата
print("Список названий банков, отсортированный по объему поступивших переводов:")
for bank_code, total_transfers in sorted_banks:
    bank_name = bank_names.get(bank_code, f"Unknown Bank {bank_code}")
    print(f"{bank_name}: {total_transfers} сом.")"""



'''Напишите регулярное выражение, которое будет искать в тексте из
файла алфавити.txt кыргызские слова длиной не менее 5 символов.'''


"""Открываем файл для чтения
with open('алфавити.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Выражение для поиска кыргызских слов длиной не менее 5 символов
regular_expression = r'\b[а-яүөәңғөчийыүі]{5,}\b'

# Находим все совпадения
matches = re.findall(regular_expression, text)

# Проходим циклом и выводим совпадения
for match in matches:
    print(match)"""


'''Напишите регулярное выражение, которое выведет список азиатских
стран, оканчивающихся на –стан, из файла asia_subregions.txt.'''


# # Открываем файл для чтения
# with open('asia_subregions.txt', 'r', encoding='utf-8') as file:
#     text = file.read()
#
# # Выражение для поиска стран, оканчивающихся на "-стан"
# regular_expression = r'\b\w+стан\b'
#
# # Находим все совпадения
# matches = re.findall(regular_expression, text)
#
# # Выводим найденные страны
# for match in matches:
#     print(match)


'''Найдите все даты в файле ulanbaatar.txt. Даты либо записаны
римскими цифрами, тогда после них написано в. либо век, века,
либо имеют слово год, года, году, г. после 4 цифр, либо имеют вид
годов жизни (четыре цифры дефис четыре цифры).'''


# Открываем файл для чтения
# with open('ulanbaatar.txt', 'r', encoding='utf-8') as file:
#     text = file.read()
#
# # Выражение для поиска дат
# regular_expression = r'\b(?:[IVX]{1,5}\.?\s*(?:века?|в\.?)|(?:\d{4}|[IVX]{1,5})\s*(?:год(?:а|у|ы|ов)?))\b|\b\d{4}-\d{4}\b'
#
# # Находим все совпадения
# matches = re.findall(regular_expression, text)
#
# # Выводим найденные даты
# for match in matches:
#     print(match)


# # 1



# import os
# import shutil
# from colorama import Fore, Back, Style
#
#
#
#
# def check_partition_exist():
#     """Проверка наличия раздела."""
#     partition_name = input("Введите имя раздела для проверки: ")
#     if os.path.exists(partition_name):
#         print(f"Раздел '{partition_name}' существует.")
#     else:
#         print(f"Раздел '{partition_name}' не существует.")
#
#
# def check_file_exist():
#     """Проверка существования файла в разделе."""
#     partition_name = input("Введите имя раздела: ")
#     file_name = input("Введите имя файла для проверки: ")
#     file_path = os.path.join(partition_name, file_name)
#     if os.path.exists(file_path):
#         print(f"Файл '{file_name}' существует в разделе '{partition_name}'.")
#     else:
#         print(f"Файл '{file_name}' не существует в разделе '{partition_name}'.")
#
#
# def create_new_partition_and_file():
#     """Создание нового раздела и файла в нем."""
#     partition_name = input("Введите имя нового раздела: ")
#     os.makedirs(partition_name, exist_ok=True)
#
#     file_name = input("Введите имя нового файла: ")
#     file_path = os.path.join(partition_name, file_name)
#
#     # Создание нового файла
#     with open(file_path, 'w') as new_file:
#         new_file.write("Это новый файл в вашем разделе.")
#
#     print(f"Создан новый файл '{file_name}' в разделе '{partition_name}'.")
#
#
# def delete_file():
#     """Удаление файла, выбранного пользователем."""
#     partition_name = input("Введите имя раздела для удаления файла: ")
#     files = os.listdir(partition_name)
#
#     if not files:
#         print("В разделе нет файлов для удаления.")
#         return
#
#     file_name = input("Введите имя файла для удаления: ")
#     file_path = os.path.join(partition_name, file_name)
#
#     if os.path.exists(file_path):
#         os.remove(file_path)
#         print(f"Файл '{file_name}' удален из раздела '{partition_name}'.")
#     else:
#         print(f"Файл '{file_name}' не существует в разделе '{partition_name}'.")
#
#
# def delete_partition():
#     """Удаление раздела."""
#     partition_name = input("Введите имя раздела для удаления: ")
#     try:
#         os.rmdir(partition_name)
#         print(f"Раздел '{partition_name}' успешно удален.")
#     except OSError as e:
#         print(Fore.RED + f"Ошибка при удалении раздела '{partition_name}': {e}")
#
#
# def delete_file_in_any_partition():
#     """Удаление файла в любом разделе, если его имя совпадает с введенным пользователем."""
#     file_name = input("Введите имя файла для удаления: ")
#     for root, dirs, files in os.walk(".", topdown=False):
#         if file_name in files:
#             file_path = os.path.join(root, file_name)
#             os.remove(file_path)
#             print(f"Файл '{file_name}' удалён из раздела '{root}'.")
#             return
#     print(f"Файл '{file_name}' не найден в каком-либо разделе.")
#
#
# def move_files_to_backup():
#     """Перемещение всех файлов в папке в подкаталог backup."""
#     partition_name = input("Введите имя раздела для перемещения файлов: ")
#     backup_dir = os.path.join(partition_name, "backup")
#
#     if not os.path.exists(partition_name):
#         print(f"Раздел '{partition_name}' не существует.")
#         return
#
#     if not os.path.exists(backup_dir):
#         os.makedirs(backup_dir)
#
#     files_moved = False
#     for file_name in os.listdir(partition_name):
#         file_path = os.path.join(partition_name, file_name)
#         if os.path.isfile(file_path):
#             shutil.move(file_path, backup_dir)
#             print(f"Файл '{file_name}' перемещён в '{backup_dir}'.")
#             files_moved = True
#
#     if not files_moved:
#         print("В разделе нет файлов для перемещения.")
#
#
# def main():
#     while True:
#         print(Fore.MAGENTA + "\nМеню операций:")
#         print(Fore.MAGENTA + "1) " + Fore.CYAN + "Проверка наличия раздела")
#         print(Fore.MAGENTA + "2) " + Fore.GREEN + "Проверка существования файла в разделе")
#         print(Fore.MAGENTA + "3) " + Fore.YELLOW + "Создание нового раздела и файла в нем")
#         print(Fore.MAGENTA + "4) " + Fore.RED + "Удаление файла из раздела")
#         print(Fore.MAGENTA + "5) " + Fore.RED + "Удаление раздела")
#         print(Fore.MAGENTA + "6) " + Fore.BLUE + "Удаление файла в любом разделе")
#         print(Fore.MAGENTA + "7) " + Fore.LIGHTMAGENTA_EX + "Перемещение файлов в backup")
#         print(Fore.MAGENTA + "8) " + Fore.BLACK + "Выход")
#
#         try:
#             choice = input(Fore.RESET + "Введите номер операции: ")
#         except KeyboardInterrupt:
#             print(Fore.RED + "\nНе делайте принудительную остановку")
#             break
#
#
#         if choice == '1':
#             check_partition_exist()
#         elif choice == '2':
#             check_file_exist()
#         elif choice == '3':
#             create_new_partition_and_file()
#         elif choice == '4':
#             delete_file()
#         elif choice == '5':
#             delete_partition()
#         elif choice == '6':
#             delete_file_in_any_partition()
#         elif choice == '7':
#             move_files_to_backup()
#         elif choice == '8':
#             print("Выход из программы.")
#             break
#         else:
#             print("Неверный выбор. Пожалуйста, выберите номер операции снова.")
#
# if __name__ == "__main__":
#             main()







# def archive_files(func):
#     '''Декоратор для копирования файлов в архивную папку'''
#     def wrapper(self, *args, **kwargs):
#         if not os.path.exists(self.archive_folder):
#             os.makedirs(self.archive_folder)
#         for file_name in [self.pin_file, self.transactions_file]:
#             if os.path.exists(file_name):
#                 shutil.copy(file_name, os.path.join(self.archive_folder, file_name))
#         return func(self, *args, **kwargs)
#     return wrapper
#
# class BankSystem:
#     ''' Класс Банковская система'''
#     def __init__(self):
#         self.pin_file = "pin.txt"
#         self.transactions_file = "transactions.txt"
#         self.accounts_folder = "accounts"
#         self.archive_folder = "archive"
#         self.pin = None
#
#     def save_pin(self, pin):
#         '''Сохраняет PIN-код в файл'''
#         with open(self.pin_file, "w") as pin_file:
#             pin_file.write(pin)
#
#     def load_pin(self):
#         '''Загружает PIN-код из файла'''
#         if os.path.exists(self.pin_file):
#             with open(self.pin_file, "r") as pin_file:
#                 return pin_file.read().strip()
#         return None
#
#     def check_pin(self):
#         '''Проверяет введенный PIN-код'''
#         correct_pin = self.load_pin()
#         if correct_pin is None:
#             return False
#
#         attempts = 0
#         while attempts < 3:
#             entered_pin = input("Введите PIN-код: ")
#             if entered_pin == correct_pin:
#                 return True
#             else:
#                 print("Неверный PIN-код. Попробуйте снова.")
#                 attempts += 1
#         return False
#
#     @archive_files
#     def create_account(self):
#         '''Создает новый счет'''
#         if not os.path.exists(self.accounts_folder):
#             os.makedirs(self.accounts_folder)
#         account_number = 1
#         while os.path.exists(os.path.join(self.accounts_folder, f"account{account_number}.txt")):
#             account_number += 1
#         with open(os.path.join(self.accounts_folder, f"account{account_number}.txt"), "w") as account_file:
#             account_file.write("0")
#         print(f"Создан новый счет: account{account_number}.txt")
#
#     @archive_files
#     def delete_account(self):
#         '''Удаляет счет'''
#         account_number = input("Введите номер счета для удаления: ")
#         account_file_path = os.path.join(self.accounts_folder, f"account{account_number}.txt")
#         if os.path.exists(account_file_path):
#             os.remove(account_file_path)
#             print(f"Счет account{account_number}.txt удален.")
#         else:
#             print("Такой счет не существует.")
#
#     # Остальные методы класса BankSystem остаются без изменений
#
# def main():
#     bank_system = BankSystem()
#
#     if not os.path.exists(bank_system.pin_file):
#         pin = input("Введите новый PIN-код для сохранения: ")
#         bank_system.save_pin(pin)
#
#     if not bank_system.check_pin():
#         print("Три неверных попытки ввода PIN-кода. Программа закрывается.")
#         return
#
#     while True:
#         print("\nМеню операций:")
#         print("1) Открыть новый счет")
#         print("2) Удалить счет")
#         print("3) Выход")
#
#         choice = input("Введите номер операции: ")
#
#         if choice == '1':
#             bank_system.create_account()
#         elif choice == '2':
#             bank_system.delete_account()
#         elif choice == '3':
#             print("Выход из программы.")
#             break
#         else:
#             print("Неверный выбор. Пожалуйста, выберите номер операции снова.")
#
# if __name__ == "__main__":
#     main()



