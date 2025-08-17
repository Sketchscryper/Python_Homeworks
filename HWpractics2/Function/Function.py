# Задание 1. Напишите функцию, которая отображает на экран форматированный текст,
# указанный ниже:
# “Don't let the noise of others' opinions
# drown out your own inner voice.”
#                             Steve Jobs

print("Задание №1.\n-------------------------------------")
def display_quote():
    print('''“Don't let the noise of others' opinions
drown out your own inner voice.”
                            Steve Jobs''')

# Вызов функции
display_quote()
print()

# Задание 2. Напишите функцию, которая принимает два числа в качестве параметра и отображает
# все нечетные числа между ними.

print("Задание №2.\n-------------------------------------")
def print_odd_numbers(start, end):
    # Определяем начальное значение для цикла
    # Если start четное, увеличиваем его на 1, чтобы начать с нечетного
    if start % 2 == 0:
        start += 1

    # Проходим по всем числам от start до end с шагом 2
    for number in range(start, end + 1, 2):
        print(number)

# Пример использования:
print_odd_numbers(1, 10) # выведет: 1, 3, 5, 7, 9
print_odd_numbers(5, 15) # выведет: 5, 7, 9, 11, 13, 15
print()

# Задание 3. Напишите функцию, которая отображает горизонтальную или вертикальную линию из
# некоторого символа. Функция принимает в качестве параметра: длину линии, направление, символ.

print("Задание №3.\n-------------------------------------")
def draw_line(length, direction, symbol):
    """
    Функция для отрисовки горизонтальной или вертикальной линии

    Параметры:
    length (int) - длина линии
    direction (str) - направление ('horizontal' или 'vertical')
    symbol (str) - символ для отрисовки линии
    """
    if direction.lower() == 'horizontal':
        # Для горизонтальной линии просто выводим символ length раз
        print(symbol * length)
    elif direction.lower() == 'vertical':
        # Для вертикальной линии выводим символ в цикле
        for _ in range(length):
            print(symbol)
    else:
        print("Ошибка: укажите направление 'horizontal' или 'vertical'")

# Примеры использования:
# Горизонтальная линия длиной 10 из символов *
draw_line(10, 'horizontal', '*') # вывод: **********

# Вертикальная линия длиной 5 из символов #
draw_line(5, 'vertical', '#') # вывод:
# #
# #
# #
# #
# #
print()

# Задание 4. Напишите функцию, которая возвращает максимальное из четырёх чисел.
# Числа передаются в качестве параметров.

print("Задание №4.\n-------------------------------------")
def find_max(a, b, c, d):
    """Возвращает максимальное из четырёх чисел через список."""
    numbers = [a, b, c, d]
    return max(numbers)

# Пример использования:
result = find_max(3, 7, 2, 9)
print(result)  # Выведет: 9
print()

# Задание 5. Напишите функцию, которая возвращает сумму чисел в указанном диапазоне.
# Границы диапазона передаются в качестве параметров.

print("Задание №5.\n-------------------------------------")
def sum_range(start, end):
    total = 0
    for number in range(start, end + 1):
        total += number
    return total

# Примеры использования:
print(sum_range(1, 5)) # Выведет: 15 (1+2+3+4+5)
print(sum_range(3, 7)) # Выведет: 25 (3+4+5+6+7)
print(sum_range(1, 11)) # Выведет: 66
print()

# Задание 6. Напишите функцию, которая проверяет является ли число простым.
# Число передаётся в качестве параметра. Если число простое нужно вернуть из метода true,
# иначе false.

print("Задание №6.\n-------------------------------------")
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# Примеры использования:
print(is_prime(2)) # True
print(is_prime(3)) # True
print(is_prime(4)) # False
print(is_prime(17)) # True
print(is_prime(18)) # False
print(is_prime(1)) # False
print()

# Задание 7. Напишите функцию, которая проверяет, является ли шестизначное число «счастливым».
# Число передаётся в качестве параметра. Если число счастливое нужно вернуть из функции true,
# иначе false. «Счастливое шестизначное число» — это число у которого сумма первых трёх цифр
# равна сумме трёх вторых цифр.
# Например, 123420 – счастливое 1+2+3 = 4+2+0, а 723422 – несчастливое 7+2+3 != 4+2+2.

print("Задание №7.\n-------------------------------------")
def is_lucky_number(number):
    # Проверяем, что число шестизначное
    if not (100000 <= number <= 999999):
        return False

    # Преобразуем число в строку для удобной работы с цифрами
    num_str = str(number)

    # Вычисляем сумму первых трёх цифр
    first_half_sum = sum(int(digit) for digit in num_str[:3])

    # Вычисляем сумму вторых трёх цифр
    second_half_sum = sum(int(digit) for digit in num_str[3:])

    # Сравниваем суммы
    return first_half_sum == second_half_sum

# Примеры использования:
print(is_lucky_number(123420)) # True, так как 1+2+3 = 4+2+0
print(is_lucky_number(723422)) # False, так как 7+2+3 != 4+2+2
print(is_lucky_number(237831)) # True, так как 2+3+7 = 8+3+1
print()


