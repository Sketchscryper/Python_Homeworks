# Задание 1. Пользователь вводит с клавиатуры три числа. В зависимости от выбора пользователя
# программа выводит на экран сумму трёх чисел или произведение трёх чисел.

first_number = float(input("Введите первое число: "))
second_number = float(input("Введите второе число: "))
third_number = float(input("Введите третье число: "))

summ = first_number + second_number + third_number
composition = first_number * second_number * third_number
action = float(input("Сумма трех чисел: (Выберите: 1)\n"
                     "Произведение трех чисел: (Выберите: 2)\n"))

if action == 1:
    print("Сумма трех чисел =", summ)
elif action == 2:
    print("Произведение трех чисел =", composition)

# Задание 2. Пользователь вводит с клавиатуры три числа.
# В зависимости от выбора пользователя программа выводит на экран максимум из трёх,
# минимум из трёх или среднеарифметическое трёх чисел.

first_number = float(input("Введите первое число: "))
second_number = float(input("Введите второе число: "))
third_number = float(input("Введите третье число: "))

action = float(input("Максимум из трех чисел: (Выберите: 1)\n"
                     "Минимум из трех чисел: (Выберите: 2)\n"
                     "Среднеарифметическое трёх чисел: (Выберите: 3)\n"))

if action == 1:
    print("Максимум из трех чисел =", max(first_number, second_number, third_number))
if action == 2:
    print("Минимум из трех чисел =", min(first_number, second_number, third_number))
if action == 3:
    print("Среднеарифметическое трёх чисел =", (first_number + second_number + third_number) / 3)

# Задание 3. Пользователь вводит с клавиатуры количество метров.
# В зависимости от выбора пользователя программа переводит метры в мили, дюймы или ярды.

number_meters = float(input("Введите количество метров: "))

action = float(input("Перевод из метров в мили: (Выберите: 1)\n"
                     "Перевод из метров в дюймы: (Выберите: 2)\n"
                     "Перевод из метров в ярды: (Выберите: 3)\n"))

if action == 1:
    print("Перевод из метров в мили =", number_meters * 0.000621)
if action == 2:
    print("Перевод из метров в дюймы =", number_meters / 0.0254)
if action == 3:
    print("Перевод из метров в ярды =", number_meters * 1.016)
