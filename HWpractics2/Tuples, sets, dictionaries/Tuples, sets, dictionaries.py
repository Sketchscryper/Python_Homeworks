# Задание 1. Пользователь вводит с клавиатуры название фрукта.
# Необходимо вывести на экран количество раз, сколько фрукт встречается в кортеже в качестве
# элемента.

print("Задание №1.\n----------------------------------")
def count_fruit(fruit_tuple, fruit_name):
    return fruit_tuple.count(fruit_name)

# Пример использования
fruits = ('apple', 'banana', 'orange', 'apple', 'mango', 'apple')
fruit_name = input("Введите название фрукта: ")
print(f"Фрукт {fruit_name} встречается {count_fruit(fruits, fruit_name)} раз.")
print()

# Задание 2. Добавьте к заданию 1 подсчет количества раз, когда название фрукта является
# частью элемента. Например: banana, apple, bananamango, mango, strawberry-banana.
# В примере выше banana встречается три раза.
print("Задание №2.\n----------------------------------")
def count_fruit_occurrences(fruit_tuple, fruit_name):
    exact_count = fruit_tuple.count(fruit_name)
    partial_count = sum(1 for fruit in fruit_tuple if fruit_name in fruit)
    return partial_count

# Пример использования
fruits = ('banana', 'apple', 'bananamango', 'mango', 'strawberry-banana')
fruit_name = input("Введите название фрукта: ")
print(f"Фрукт {fruit_name} встречается {count_fruit_occurrences(fruits, fruit_name)} раз (включая частичные совпадения).")
print()

# Задание 3. Есть кортеж с названиями производителей автомобилей
# (название производителя может встречаться от 0 до N раз).
# Пользователь вводит с клавиатуры название производителя и слово для замены.
# Необходимо заменить в кортеже все элементы с этим названием на слово для замены.
# Совпадение по названию должно быть полным.
print("Задание №3.\n----------------------------------")
def replace_manufacturer(manufacturers, old_name, new_name):
    return tuple(new_name if manufacturer == old_name else manufacturer for manufacturer in manufacturers)

# Пример использования
manufacturers = ('Toyota', 'BMW', 'Lada', 'Mercedes', 'Porsche', 'BMW')
old_name = input("Введите название производителя для замены: ")
new_name = input("Введите новое название: ")
updated_manufacturers = replace_manufacturer(manufacturers, old_name, new_name)
print("Обновленный кортеж:", updated_manufacturers)
print()

# Задание 4. Есть кортеж с целыми числами.
# Нужно вывести статистику по количеству цифр в элементах кортежа. Например:
# ■ Одна цифра — 3 элемента;
# ■ Две цифры — 4 элемента;
# ■ Три цифры — 5 элементов.

print("Задание №4.\n----------------------------------")
def count_digits_stats(numbers_tuple):
    stats = {}
    for number in numbers_tuple:
        digit_count = len(str(abs(number)))
        if digit_count in stats:
            stats[digit_count] += 1
        else:
            stats[digit_count] = 1

    # Форматируем вывод
    for digit_count in sorted(stats.keys()):
        print(f"■ {digit_count} цифра — {stats[digit_count]} элементов")

# Пример использования
numbers = (1, 23, 456, 7, 89, 12, 345, 6789, 123)
count_digits_stats(numbers)
print()

