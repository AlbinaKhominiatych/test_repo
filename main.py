#1
try:
    number = float(input("Введіть число: "))
    print(f"Ви ввели: {number}")
except ValueError as e:
    print(f"Помилка: {e}. Введено не число.")

#2
def serednie_arifmetichne(spysok):
    try:
        seredne = sum(spysok) / len(spysok)
        return seredne
    except ZeroDivisionError:
        return "Список порожній. Неможливо знайти середнє арифметичне."

# Приклад використання:
numbers = [10, 20, 30, 40, 50]
result = serednie_arifmetichne(numbers)
print(result)  # Виведе: 30.0

empty_list = []
result_empty = serednie_arifmetichne(empty_list)
print(result_empty)  # Виведе: Список порожній. Неможливо знайти середнє арифметичне.


#3
def to_string(value):
    try:
        result = str(value)
        return result
    except Exception as e:
        return f"Помилка: аргумент не може бути перетворений у рядок. Деталі: {e}"

# Приклад використання:
value1 = 123
string_value1 = to_string(value1)
print(string_value1)  # Виведе: '123'

value2 = None
string_value2 = to_string(value2)
print(string_value2)  # Виведе: "Помилка: аргумент не може бути перетворений у рядок. Деталі: 'NoneType' object is not str"

#4
def remove_element_from_list(my_list, element):
    try:
        my_list.remove(element)
        return my_list
    except ValueError as e:
        return f"Помилка: {e}"

# Приклад використання:
result = remove_element_from_list([1, 2, 3, 4, 5], 3)
print(result)  # Виведе: [1, 2, 4, 5]

result_not_in_list = remove_element_from_list([1, 2, 3, 4, 5], 6)
print(result_not_in_list)  # Виведе: Помилка: list.remove(x): x not in list

#5
import random
import string

def generate_random_password(length):
    try:
        if length <= 0:
            raise ValueError("Довжина паролю повинна бути більше 0.")
        password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length))
        return password
    except ValueError as e:
        return str(e)

# Приклад використання:
try:
    password_length = int(input("Введіть довжину паролю: "))
    password = generate_random_password(password_length)
    print(f"Згенерований пароль: {password}")
except ValueError as e:
    print(f"Помилка: {e}")

#6
def factorial(n):
    try:
        if n < 0:
            raise ValueError("Факторіал не визначений для від'ємних чисел.")
        if n == 0 or n == 1:
            return 1
        else:
            return n * factorial(n-1)
    except ValueError as e:
        return str(e)

# Приклад використання:
try:
    number = int(input("Введіть ціле число: "))
    result = factorial(number)
    print(f"Факторіал числа {number} = {result}")
except ValueError as e:
    print(f"Помилка: {e}")

#7
from datetime import datetime

def validate_date(date_string):
    try:
        datetime.strptime(date_string, '%d/%m/%Y')
        return True
    except ValueError:
        return False

# Приклад використання:
date_input = input("Введіть дату у форматі 'dd/mm/yyyy': ")

if validate_date(date_input):
    print(f"Введена дата {date_input} є правильною.")
else:
    print(f"Введена дата {date_input} є неправильною або не відповідає формату 'dd/mm/yyyy'.")

#8
def manipulate_dictionary(my_dict, action, key, value=None):
    try:
        if action == 'додати':
            my_dict[key] = value
        elif action == 'оновити':
            if key in my_dict:
                my_dict[key] = value
            else:
                raise KeyError(f"Ключ '{key}' не існує у словнику.")
        elif action == 'видалити':
            if key in my_dict:
                del my_dict[key]
            else:
                raise KeyError(f"Ключ '{key}' не існує у словнику.")
        else:
            raise ValueError("Некоректна дія. Використовуйте 'додати', 'оновити' або 'видалити'.")
    except (ValueError, KeyError) as e:
        return str(e)

# Приклад використання:
my_dict = {'a': 1, 'b': 2, 'c': 3}

result_add = manipulate_dictionary(my_dict, 'додати', 'd', 4)
print(result_add)  # Виведе: None, оскільки додавання пройшло успішно

result_update = manipulate_dictionary(my_dict, 'оновити', 'b', 5)
print(result_update)  # Виведе: None, оскільки оновлення пройшло успішно

result_delete = manipulate_dictionary(my_dict, 'видалити', 'c')
print(result_delete)  # Виведе: None, оскільки видалення пройшло успішно

result_invalid_action = manipulate_dictionary(my_dict, 'невідома_дія', 'x')
print(result_invalid_action)  # Виведе: Некоректна дія. Використовуйте 'додати', 'оновити' або 'видалити'.

result_invalid_key = manipulate_dictionary(my_dict, 'оновити', 'z', 6)
print(result_invalid_key)  # Виведе: Ключ 'z' не існує у словнику.


#9
import random

def roll_dice():
    try:
        sides = int(input("Введіть кількість граней кубика: "))
        if sides <= 0:
            raise ValueError("Кількість граней кубика повинна бути більше 0.")
        result = random.randint(1, sides)
        return result
    except ValueError as e:
        return str(e)

# Приклад використання:
try:
    dice_result = roll_dice()
    if isinstance(dice_result, int):
        print(f"Ви кинули кубик і вам випало: {dice_result}")
    else:
        print(f"Помилка: {dice_result}")
except Exception as e:
    print(f"Помилка: {e}")


