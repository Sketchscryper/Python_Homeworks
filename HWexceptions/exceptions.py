# 1. Напиши функцию divide(a, b), которая возвращает результат деления a на b.
# Обработай исключение ZeroDivisionError, если b = 0, и верни "Деление на ноль!".

def divide(a, b):
    """
    Функция для деления числа a на число b

    Параметры:
    a (float или int) - делимое
    b (float или int) - делитель

    Возвращает:
    float - результат деления

    Вызывает:
    ZeroDivisionError - если делитель равен нулю
    TypeError - если переданы неподдерживаемые типы данных
    """
    try:
        # Проверяем типы данных
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Оба аргумента должны быть числами (int или float)")

        # Проверяем деление на ноль
        if b == 0:
            raise ZeroDivisionError("Деление на ноль!")

        # Выполняем деление
        return a / b

    except TypeError as te:
        print(f"Ошибка типа: {te}")
    except ZeroDivisionError as ve:
        print(f"Математическая ошибка: {ve}")

# Примеры использования:
print("Задание №1.\n-------------------------")
print(divide(10, 2))  # 5.0
print(divide(5, 0))  # Математическая ошибка: Деление на ноль!
print(divide("5", 2))  # Ошибка типа: Оба аргумента должны быть числами (int или float)
print()

# 2. Напиши функцию get_element(arr, index), которая возвращает элемент списка arr по индексу index.
# Обработай IndexError и TypeError, возвращая "Ошибка доступа к элементу".

def get_element(arr, index):
    """
    Функция для получения элемента списка по индексу

    Параметры:
    arr (list) - список, из которого нужно получить элемент
    index (int) - индекс элемента

    Возвращает:
    элемент списка по указанному индексу
    или "Ошибка доступа к элементу" при возникновении ошибки
    """
    try:
        # Проверяем, что arr является списком
        if not isinstance(arr, list):
            raise TypeError("Первый аргумент должен быть списком")

        # Проверяем, что index является целым числом
        if not isinstance(index, int):
            raise TypeError("Индекс должен быть целым числом")

        # Возвращаем элемент по индексу
        return arr[index]

    except (IndexError, TypeError):
        return "Ошибка доступа к элементу"


# Примеры использования:
print("Задание №2.\n-------------------------")
print(get_element([1, 2, 3], 1))  # Выведет: 2
print(get_element([1, 2, 3], 5))  # Выведет: Ошибка доступа к элементу
print(get_element([1, 2, 3], 'a')) # Выведет: Ошибка доступа к элементу
print(get_element('строка', 1))  # Выведет: Ошибка доступа к элементу
print()

# 3. Напиши функцию check_age(age), которая вызывает ValueError
# с сообщением "Возраст не может быть отрицательным!", если age < 0,
# и "Слишком большой возраст!", если age > 120.

def check_age(age):
    """
    Функция проверки корректности возраста

    Параметры:
    age (int) - возраст для проверки

    Вызывает:
    ValueError - при некорректном значении возраста
    """
    try:
        # Проверяем, что возраст не отрицательный
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным!")

        # Проверяем, что возраст не превышает 120 лет
        if age > 120:
            raise ValueError("Слишком большой возраст!")

        # Если все проверки пройдены, возвращаем True
        return True

    except ValueError as e:
        # Выводим сообщение об ошибке
        print(f"Ошибка: {e}")
        raise  # Перебрасываем исключение дальше


# Примеры использования:
print("Задание №3.\n-------------------------")
try:
    check_age(-5)  # Вызовет ошибку "Возраст не может быть отрицательным!"
except ValueError as e:
    print(e)

try:
    check_age(150)  # Вызовет ошибку "Слишком большой возраст!"
except ValueError as e:
    print(e)

try:
    check_age(25)  # Пройдет успешно
except ValueError as e:
    print(e)
print()

# 4. Напиши функцию read_file(filename), которая читает файл и возвращает его содержимое.
# Обработай FileNotFoundError, возвращая "Файл не найден".

def read_file(filename):
    """
    Функция для чтения содержимого файла

    Параметры:
    filename (str) - путь к файлу

    Возвращает:
    Содержимое файла в виде строки
    или "Файл не найден" при ошибке
    """
    try:
        # Открываем файл в режиме чтения
        with open(filename, 'r', encoding='utf-8') as file:
            # Читаем содержимое файла
            content = file.read()
            return content

    except FileNotFoundError:
        # Обработка ошибки, если файл не найден
        return "Файл не найден"

    except Exception as e:
        # Обработка других возможных ошибок
        return f"Произошла ошибка: {str(e)}"

# Примеры использования:
print("Задание №4.\n-------------------------")
print(read_file('example.txt'))  # Если файл существует
print(read_file('non_existent.txt'))  # Вернет "Файл не найден"
print()

# 5. Напиши функцию convert_to_int(s), которая преобразует строку s в число.
# Обработай ValueError, возвращая "Нельзя преобразовать в число".

def convert_to_int(s):
    """
    Функция для преобразования строки в целое число

    Параметры:
    s (str) - строка для преобразования

    Возвращает:
    int - преобразованное число
    или "Нельзя преобразовать в число" при ошибке
    """
    try:
        # Пытаемся преобразовать строку в целое число
        number = int(s)
        return number

    except ValueError:
        # Обрабатываем ошибку при невозможности преобразования
        return "Нельзя преобразовать в число"


# Примеры использования:
print("Задание №5.\n-------------------------")
print(convert_to_int("123")) # Выведет: 123
print(convert_to_int("45.6")) # Выведет: Нельзя преобразовать в число
print(convert_to_int("abc")) # Выведет: Нельзя преобразовать в число
print(convert_to_int("  789  ")) # Выведет: 789 (пробелы игнорируются)
print(convert_to_int("-42")) # Выведет: -42
print()

# 6. Напиши функцию dict_lookup(d, key), которая возвращает значение из словаря d по ключу key.
# Обработай KeyError, возвращая "Ключ не найден".

def dict_lookup(d, key):
    """
    Функция для получения значения из словаря по ключу

    Параметры:
    d (dict) - словарь для поиска
    key - ключ, по которому производится поиск

    Возвращает:
    Значение из словаря, если ключ найден
    "Ключ не найден", если ключ отсутствует
    """
    try:
        # Пытаемся получить значение по ключу
        return d[key]

    except KeyError:
        # Обрабатываем ошибку отсутствия ключа
        return "Ключ не найден"

    except TypeError:
        # Обрабатываем случай, если передан не словарь
        return "Неверный тип данных"


# Примеры использования:
user_data = {
    'name': 'Иван',
    'age': 25,
    'city': 'Москва'
}
print("Задание №6.\n-------------------------")
print(dict_lookup(user_data, 'name')) # Выведет: Иван
print(dict_lookup(user_data, 'age')) # Выведет: 25
print(dict_lookup(user_data, 'email')) # Выведет: Ключ не найден
print(dict_lookup([1, 2, 3], 'name')) # Выведет: Неверный тип данных
print()

# 7. Напиши функцию sqrt_or_error(x), которая возвращает квадратный корень из x.
# Обработай ValueError (если x < 0), возвращая "Число должно быть неотрицательным".

import math

def sqrt_or_error(x):
    """
    Функция для вычисления квадратного корня числа

    Параметры:
    x (float или int) - число, из которого извлекается корень

    Возвращает:
    float - квадратный корень числа
    или "Число должно быть неотрицательным" при ошибке
    """
    try:
        # Проверяем, что число неотрицательное
        if x < 0:
            raise ValueError("Число должно быть неотрицательным")

        # Вычисляем квадратный корень
        return math.sqrt(x)

    except ValueError as e:
        # Возвращаем сообщение об ошибке
        return str(e)


# Примеры использования:
print("Задание №7.\n-------------------------")
print(sqrt_or_error(9)) # Выведет: 3.0
print(sqrt_or_error(0)) # Выведет: 0.0
print(sqrt_or_error(-4)) # Выведет: Число должно быть неотрицательным
print(sqrt_or_error(2.25)) # Выведет: 1.5
print()

# 8. Напиши функцию connect_to_db(url), которая имитирует подключение к БД.
# Если url некорректен, вызови ConnectionError с сообщением "Не удалось подключиться".

def connect_to_db(url):
    """
    Функция для имитации подключения к базе данных

    Параметры:
    url (str) - URL подключения к базе данных

    Вызывает:
    ConnectionError - при некорректном URL
    """
    try:
        # Простая проверка корректности URL
        if not isinstance(url, str):
            raise ConnectionError("Не удалось подключиться")

        if not url.startswith(("postgresql://", "mysql://", "sqlite://")):
            raise ConnectionError("Не удалось подключиться")

        # Имитация успешного подключения
        print("Подключение установлено")
        return True

    except ConnectionError as e:
        print(f"Ошибка: {str(e)}")
        raise


# Примеры использования:
print("Задание №8.\n-------------------------")
try:
    connect_to_db("postgresql://localhost:5432/mydb")  # Успешное подключение
except ConnectionError as e:
    print(e)

try:
    connect_to_db("http://localhost:5432/mydb")  # Некорректный URL
except ConnectionError as e:
    print(e)

try:
    connect_to_db(12345)  # Некорректный тип данных
except ConnectionError as e:
    print(e)
print()

# 9. Напиши функцию process_data(data), которая обрабатывает данные.
# Если data не является списком, вызови TypeError.
# Если список пуст, вызови ValueError с сообщением "Нет данных".

def process_data(data):
    """
    Функция для обработки данных

    Параметры:
    data (list) - данные для обработки

    Вызывает:
    TypeError - если data не является списком
    ValueError - если список пуст
    """
    try:
        # Проверяем, что данные являются списком
        if not isinstance(data, list):
            raise TypeError("Данные должны быть списком")

        # Проверяем, что список не пустой
        if len(data) == 0:
            raise ValueError("Нет данных")

        # Здесь можно добавить реальную обработку данных
        print("Данные успешно обработаны")
        return data

    except TypeError as te:
        print(f"Ошибка типа: {te}")
        raise

    except ValueError as ve:
        print(f"Ошибка значения: {ve}")
        raise


# Примеры использования:
print("Задание №9.\n-------------------------")
try:
    process_data([1, 2, 3])  # Успешная обработка
except Exception as e:
    print(e)

try:
    process_data("")  # Вызовет TypeError
except Exception as e:
    print(e)

try:
    process_data([])  # Вызовет ValueError
except Exception as e:
    print(e)
print()

# 10. Напиши класс Validator с методом validate_email(email), который проверяет,
# содержит ли email символ @. Если нет, вызови ValueError с сообщением "Некорректный email".

class Validator:
    """
    Класс для валидации данных
    """

    def validate_email(self, email):
        """
        Метод для проверки корректности email

        Параметры:
        email (str) - адрес электронной почты для проверки

        Вызывает:
        ValueError - если email некорректный
        """
        try:
            # Проверяем, что email содержит символ @
            if not isinstance(email, str):
                raise ValueError("Email должен быть строкой")

            if '@' not in email:
                raise ValueError("Некорректный email")

            # Простая проверка наличия точки после @
            if email.count('@') != 1 or '.' not in email.split('@')[1]:
                raise ValueError("Некорректный email")

            print("Email корректен")
            return True

        except ValueError as ve:
            print(f"Ошибка валидации: {ve}")
            raise


# Примеры использования:
print("Задание №10.\n-------------------------")
validator = Validator()

try:
    validator.validate_email("test@example.com")  # Корректный email
except ValueError as e:
    print(e)

try:
    validator.validate_email("testexample.com")  # Отсутствует @
except ValueError as e:
    print(e)

try:
    validator.validate_email(12345)  # Не строка
except ValueError as e:
    print(e)
