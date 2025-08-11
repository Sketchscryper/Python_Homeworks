# Задание №1. Простая арифметика.
# Напишите программу, которая запрашивает у пользователя два числа и выводит их сумму,
# разность, произведение и частное.

print("Задание №1.\n--------------------------")
# Запрашиваем у пользователя два числа
a = float(input('Введите первое число: '))
b = float(input('Введите второе число: '))

# Выводим результаты вычислений
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")

# Проверяем деление на ноль
if b != 0:
    print(f"{a} / {b} = {a / b}")
else:
    print("Деление на ноль невозможно!")
print()

# Задание №2. Чётное или нечётное? Напишите программу, которая принимает число и выводит
# "Чётное", если число делится на 2, и "Нечётное" в противном случае.

print("Задание №2.\n--------------------------")
# Получаем число от пользователя
number = int(input("Введите число: "))

# Проверяем чётность
if number % 2 == 0:
    print("Чётное")
else:
    print("Нечётное")
print()

# Задание №3. Факториал числа. Напишите функцию, которая вычисляет факториал
# числа n (произведение всех чисел от 1 до n). Пример: Ввод: 5 → Вывод: 120 (1×2×3×4×5).

print("Задание №3.\n--------------------------")
# Рекурсивный вариант
def factorial_recursive(n):
    if n == 0:
        return 1
    return n * factorial_recursive(n - 1)

# Итеративный вариант
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Пример использования
number = int(input("Введите число: "))
print(f"Факториал числа {number}:")
print("Рекурсивный:", factorial_recursive(number))
print("Итеративный:", factorial_iterative(number))
print()

# Задание №4. Поиск максимального числа в списке.
# Напишите функцию, которая принимает список чисел и возвращает наибольшее из них.
# Пример: Ввод: [3, 7, 2, 9, 1] → Вывод: 9.

print("Задание №4.\n--------------------------")
# Задаем функцию для поиска максимума из списка чисел
def find_max(numbers):
    return max(numbers)

# Пример использования
numbers = [3, 7, 2, 9, 1]
print(find_max(numbers))  # Вывод: 9
print()

# Задание №5. Палиндром. Напишите функцию, которая проверяет,
# является ли строка палиндромом (читается одинаково слева направо и справа налево).
# Пример: Ввод: "топот" → Вывод: True Ввод: "python" → Вывод: False.

print("Задание №5.\n--------------------------")
# Задаем функцию для проверки на палиндром
def is_palindrome(s):
    s = s.replace(" ", "").lower()  # Убираем пробелы и приводим к нижнему регистру
    return s == s[::-1]

# Примеры использования
print(is_palindrome("топот")) # True
print(is_palindrome("А роза упала на лапу Азора")) # True
print()

# Задание №6. Подсчёт гласных. Напишите функцию, которая считает количество гласных
# букв (a, e, i, o, u) в строке. Пример: Ввод: "Hello, World!" → Вывод: 3(e, o, o).

print("Задание №6.\n--------------------------")
def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)

# Примеры использования
print(count_vowels("Hello, World!"))  # Вывод: 3
print(count_vowels("Python"))         # Вывод: 1
print()

# Задание №7. Генератор паролей. Напишите функцию, которая генерирует случайный пароль
# заданной длины (используйте буквы, цифры и символы).
# Пример: Ввод: 8 → Вывод: "aB3$k9Lm" (случайная комбинация)/.

print("Задание №7.\n--------------------------")
import random
import string

def generate_password(length, use_lower=True, use_upper=True, use_digits=True, use_special=True):
    if length < 1:
        raise ValueError("Длина пароля должна быть больше 0")

    # Формируем набор символов на основе настроек
    characters = ''
    if use_lower:
        characters += string.ascii_lowercase
    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        raise ValueError("Должен быть выбран хотя бы один тип символов")

    return ''.join(random.choice(characters) for _ in range(length))

# Примеры использования
print(generate_password(8))  # Все типы символов по умолчанию
print(generate_password(8, use_special=False))  # Без специальных символов
print()

# Задание №8. Разворот списка. Напишите функцию, которая переворачивает список без использования
# встроенного метода .reverse(). Пример: Ввод: [1, 2, 3, 4] → Вывод: [4, 3, 2, 1].

print("Задание №8.\n--------------------------")

def reverse_list(lst):
    return lst[::-1]

# Пример использования
print(reverse_list([1, 2, 3, 4]))  # Вывод: [4, 3, 2, 1]
print()

# Задание №9. Фильтрация списка. Напишите функцию, которая принимает список чисел и возвращает
# новый список, содержащий только чётные числа.
# Пример: Ввод: [1, 2, 3, 4, 5, 6] → Вывод: [2, 4, 6].

print("Задание №9.\n--------------------------")
# Задаем функцию, которая возвращает список, содержащий только четные числа
def filter_even_numbers(numbers):
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers

# Пример использования
print(filter_even_numbers([1, 2, 3, 4, 5, 6]))  # Вывод: [2, 4, 6]
print()

# Задание №10. Калькулятор времени. Напишите функцию, которая принимает количество секунд и
# возвращает строку в формате "Дни:Час:Мин:Сек".
# Пример: Ввод: 100000 → Вывод: "1:3:46:40" (1 день, 3 часа, 46 минут, 40 секунд)”.

print("Задание №10.\n--------------------------")
def convert_seconds(seconds):
    if not isinstance(seconds, int) or seconds < 0:
        raise ValueError("Время должно быть неотрицательным целым числом")

    days = seconds // (24 * 3600)
    seconds %= (24 * 3600)
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    return f"{days}:{hours}:{minutes}:{seconds}"

# Примеры использования
try:
    print(convert_seconds(100000))  # Вывод: "1:3:46:40"
    print(convert_seconds(-100))  # Вызовет ошибку
except ValueError as e:
    print(e)
