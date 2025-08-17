# Задание 1. Пользователь вводит число. Определить количество цифр в этом числе,
# посчитать их сумму и среднее арифметическое. Определить количество нулей в этом числе.
# Общение с пользователем организовать через меню.
print("Задание №1.\n------------------------------")
def analyze_number():
    while True:
        print("Меню:")
        print("1. Ввести число")
        print("2. Показать результаты анализа")
        print("3. Выйти")

        choice = input("Выберите пункт меню: ")

        if choice == '1':
            try:
                number = int(input("Введите целое число: "))
                # Сохраняем абсолютное значение для корректной обработки отрицательных чисел
                abs_number = abs(number)
                # Создаем копию числа для анализа
                temp = abs_number

                # Инициализация переменных
                digit_count = 0
                sum_digits = 0
                zero_count = 0

                # Анализ цифр числа
                while temp > 0:
                    digit = temp % 10
                    sum_digits += digit
                    if digit == 0:
                        zero_count += 1
                    digit_count += 1
                    temp = temp // 10

                # Если число состоит только из нулей
                if digit_count == 0:
                    digit_count = 1
                    zero_count = 1

                # Сохраняем результаты анализа
                results = {
                    'number': number,
                    'digit_count': digit_count,
                    'sum_digits': sum_digits,
                    'zero_count': zero_count,
                    'average': sum_digits / digit_count
                }
                print("Число успешно введено и проанализировано!")

            except ValueError:
                print("Ошибка: введите корректное целое число!")

        elif choice == '2':
            try:
                # Проверяем, были ли введены данные
                print(f"\nАнализ числа {results['number']}:")
                print(f"Количество цифр: {results['digit_count']}")
                print(f"Сумма цифр: {results['sum_digits']}")
                print(f"Среднее арифметическое: {results['average']:.2f}")
                print(f"Количество нулей: {results['zero_count']}")

            except NameError:
                print("Ошибка: сначала введите число!")

        elif choice == '3':
            print("Программа завершена.")
            break

        else:
            print("Неверный выбор. Попробуйте еще раз.")


# Запуск программы
analyze_number()
print()

# Задание 2. Написать программу, которая выводит на экран шахматную доску с заданным размером
# клеточки. Например, три,
# ***---***---***---***---
# ***---***---***---***---
# ***---***---***---***---
# ---***---***---***---***
# ---***---***---***---***
# ---***---***---***---***

print("Задание №2.\n------------------------------")
def print_chess_board(size, cell_size):
    # Определяем символы для черных и белых клеток
    black_cell = '*' * cell_size
    white_cell = '-' * cell_size

    # Создаем разделитель между строками
    separator = '\n' + '-' * (size * (cell_size + 1) - 1) + '\n'

    for row in range(size):
        line = ''
        # Определяем, с какой клетки начинать строку
        start_with_black = (row % 2 == 0)

        for col in range(size):
            if start_with_black:
                line += black_cell + '-'
                start_with_black = False
            else:
                line += white_cell + '-'
                start_with_black = True

        # Удаляем последний символ '-' в строке
        line = line[:-1]
        print(line)

        # Добавляем разделитель между строками
        if row < size - 1:
            print(separator)

def main():
    try:
        # Получаем размер доски и размер клетки от пользователя
        size = int(input("Введите размер доски (количество клеток по стороне): "))
        cell_size = int(input("Введите размер клетки (количество символов): "))

        # Выводим шахматную доску
        print("\nШахматная доска:")
        print_chess_board(size, cell_size)

    except ValueError:
        print("Ошибка: введите целые положительные числа!")

if __name__ == "__main__":
    main()
print()

# Задание 3. Написать программу, которая проверяет пользователя на знание таблицы умножения.
# Программа выводит на экран два числа, пользователь должен ввести их произведение.
# Разработать несколько уровней сложности (отличаются сложностью и количеством вопросов).
# Вывести пользователю оценку его знаний.

print("Задание №3.\n------------------------------")
import random

def generate_question(level):
    """Генерация вопроса в зависимости от уровня сложности"""
    if level == 1:
        # Легкий уровень: числа от 1 до 5
        num1 = random.randint(1, 5)
        num2 = random.randint(1, 5)
    elif level == 2:
        # Средний уровень: числа от 1 до 10
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
    else:
        # Сложный уровень: числа от 1 до 12
        num1 = random.randint(1, 12)
        num2 = random.randint(1, 12)
    return num1, num2

def main():
    print("Проверка знания таблицы умножения")
    print("Выберите уровень сложности:")
    print("1 - Легкий (5 вопросов, числа до 5)")
    print("2 - Средний (10 вопросов, числа до 10)")
    print("3 - Сложный (15 вопросов, числа до 12)")

    try:
        level = int(input("Ваш выбор (1-3): "))
        if level < 1 or level > 3:
            print("Неверный выбор уровня!")
            return

        # Устанавливаем количество вопросов в зависимости от уровня
        if level == 1:
            questions = 5
        elif level == 2:
            questions = 10
        else:
            questions = 15

        correct = 0

        for i in range(questions):
            num1, num2 = generate_question(level)
            try:
                answer = int(input(f"\nВопрос {i + 1}: {num1} * {num2} = "))
                if answer == num1 * num2:
                    print("Правильно!")
                    correct += 1
                else:
                    print(f"Неправильно. Правильный ответ: {num1 * num2}")
            except ValueError:
                print("Ошибка: введите число!")

        # Выводим результаты
        print("\nРезультаты теста:")
        print(f"Правильных ответов: {correct} из {questions}")
        percentage = (correct / questions) * 100

        if percentage >= 90:
            print("Ваша оценка: 5 (отлично)")
        elif percentage >= 75:
            print("Ваша оценка: 4 (хорошо)")
        elif percentage >= 50:
            print("Ваша оценка: 3 (удовлетворительно)")
        else:
            print("Ваша оценка: 2 (неудовлетворительно)")

    except ValueError:
        print("Ошибка: введите число от 1 до 3!")

if __name__ == "__main__":
    main()
print()

# Задание 4. Вывести на экран ромб из звездочек.
print("Задание №4.\n------------------------------")

def print_diamond(size):
    # Проверяем, что размер нечетный
    if size % 2 == 0:
        print("Размер должен быть нечетным числом!")
        return

    # Верхняя часть ромба
    for i in range(size // 2 + 1):
        # Выводим пробелы
        for j in range(size // 2 - i):
            print(" ", end="")
        # Выводим звездочки
        for k in range(2 * i + 1):
            print("*", end="")
        print()  # Переход на новую строку

    # Нижняя часть ромба
    for i in range(size // 2 - 1, -1, -1):
        # Выводим пробелы
        for j in range(size // 2 - i):
            print(" ", end="")
        # Выводим звездочки
        for k in range(2 * i + 1):
            print("*", end="")
        print()  # Переход на новую строку

def main():
    try:
        size = int(input("Введите размер ромба (нечетное число): "))
        print("\nРомб из звездочек:")
        print_diamond(size)
    except ValueError:
        print("Ошибка: введите целое число!")

if __name__ == "__main__":
    main()
print()

