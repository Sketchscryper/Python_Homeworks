# Задание 1. Пользователь вводит с клавиатуры строку. Произведите поворот строк и
# полученный результат выведите на экран.

print("Задание №1.\n----------------------------")
def reverse_string_slice(text):
    return text[::-1]

# Пример использования
user_input = input("Введите строку: ")
result = reverse_string_slice(user_input)
print("Перевернутая строка:", result)
print()

# Задание 2. Пользователь вводит с клавиатуры строку. Посчитайте количество букв, цифр в строке.
# Выведите оба количества на экран.

print("Задание №2.\n----------------------------")
def count_letters_and_digits(text):
    letters_count = 0
    digits_count = 0

    for char in text:
        if char.isalpha():  # Проверяем, является ли символ буквой
            letters_count += 1
        elif char.isdigit():  # Проверяем, является ли символ цифрой
            digits_count += 1

    return letters_count, digits_count

def main():
    # Получаем ввод от пользователя
    user_input = input("Введите строку: ")

    # Подсчитываем буквы и цифры
    letters, digits = count_letters_and_digits(user_input)

    # Выводим результаты
    print(f"\nКоличество букв: {letters}")
    print(f"Количество цифр: {digits}")

if __name__ == "__main__":
    main()
print()

# Задание 3. Пользователь вводит с клавиатуры строку и символ для поиска.
# Посчитайте сколько раз в строке встречается искомый символ.
# Полученное число выведите на экран.

print("Задание №3.\n----------------------------")
def count_symbol_occurrences():
    # Получаем ввод от пользователя
    text = input("Введите строку: ")
    symbol = input("Введите символ для поиска: ")

    # Проверяем, что введен ровно один символ
    if len(symbol) != 1:
        print("Ошибка: нужно ввести ровно один символ!")
        return

    # Подсчитываем количество вхождений
    count = text.count(symbol)

    # Выводим результат
    print(f"\nСимвол '{symbol}' встречается в строке {count} раз(а)")

def main():
    try:
        count_symbol_occurrences()
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")

if __name__ == "__main__":
    main()
print()

# Задание 4. Пользователь вводит с клавиатуры строку и слово для поиска.
# Посчитайте сколько раз в строке встречается искомое слово.
# Полученное число выведите на экран.

print("Задание №4.\n----------------------------")
def count_word_occurrences():
    # Получаем ввод от пользователя
    text = input("Введите строку: ").lower()
    search_word = input("Введите слово для поиска: ").lower()
    # Разбиваем текст на слова
    words = text.split()

    # Подсчитываем количество вхождений слова
    count = words.count(search_word)

    # Выводим результат
    print(f"\nСлово '{search_word}' встречается в строке {count} раз(а)")

def main():
    try:
        count_word_occurrences()
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")

if __name__ == "__main__":
    main()
print()

# Задание 5. Пользователь вводит с клавиатуры строку, слово для поиска, слово для замены.
# Произведите в строке замену одного слова на другое.
# Полученную строку отобразите на экране.

print("Задание №5.\n----------------------------")
def replace_words():
    # Получаем ввод от пользователя
    original_text = input("Введите исходную строку: ")
    search_word = input("Введите слово для поиска: ")
    replace_word = input("Введите слово для замены: ")

    # Производим замену
    modified_text = original_text.replace(search_word, replace_word)

    # Выводим результат
    print("\nИсходная строка:")
    print(original_text)
    print("\nРезультат замены:")
    print(modified_text)


def main():
    try:
        replace_words()
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")


if __name__ == "__main__":
    main()
