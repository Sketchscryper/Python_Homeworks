# Задание 1. Реализуйте класс «Человек».
# Необходимо хранить в полях класса: ФИО, дату рождения, контактный телефон,
# город, страну, домашний адрес. Реализуйте методы класса для ввода данных, вывода данных,
# реализуйте доступ к отдельным полям через методы класса.

print("Задание №1.\n----------------------------------")
class Human:
    def __init__(self, full_name="", birth_date="", phone="", city="", country="", address=""):
        self.__full_name = full_name
        self.__birth_date = birth_date
        self.__phone = phone
        self.__city = city
        self.__country = country
        self.__address = address

    # Методы ввода данных
    def input_data(self):
        self.__full_name = input("Введите ФИО: ")
        self.__birth_date = input("Введите дату рождения: ")
        self.__phone = input("Введите контактный телефон: ")
        self.__city = input("Введите город: ")
        self.__country = input("Введите страну: ")
        self.__address = input("Введите домашний адрес: ")

    # Методы вывода данных
    def display_data(self):
        print(f"ФИО: {self.__full_name}")
        print(f"Дата рождения: {self.__birth_date}")
        print(f"Контактный телефон: {self.__phone}")
        print(f"Город: {self.__city}")
        print(f"Страна: {self.__country}")
        print(f"Домашний адрес: {self.__address}")

    # Геттеры и сеттеры
    def get_full_name(self):
        return self.__full_name

    def set_full_name(self, full_name):
        self.__full_name = full_name

    def get_birth_date(self):
        return self.__birth_date

    def set_birth_date(self, birth_date):
        self.__birth_date = birth_date

    def get_phone(self):
        return self.__phone

    def set_phone(self, phone):
        self.__phone = phone

    def get_city(self):
        return self.__city

    def set_city(self, city):
        self.__city = city

    def get_country(self):
        return self.__country

    def set_country(self, country):
        self.__country = country

    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address

# Примеры использования
person = Human()
person.input_data()
person.display_data()
person.set_phone("+1234567890")
print(person.get_phone())
print()

# Задание 2. Создайте класс «Город».
# Необходимо хранить в полях класса: название города, название региона, название
# страны, количество жителей в городе, почтовый индекс города, телефонный код города.
# Реализуйте методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным
# полям через методы класса.

print("Задание №2.\n----------------------------------")
class City:
    def __init__(self, name="", region="", country="", population=0, postal_code="", phone_code=""):
        self.__name = name
        self.__region = region
        self.__country = country
        self.__population = population
        self.__postal_code = postal_code
        self.__phone_code = phone_code

    # Методы ввода данных
    def input_data(self):
        self.__name = input("Введите название города: ")
        self.__region = input("Введите название региона: ")
        self.__country = input("Введите название страны: ")
        self.__population = int(input("Введите количество жителей: "))
        self.__postal_code = input("Введите почтовый индекс: ")
        self.__phone_code = input("Введите телефонный код: ")

    # Методы вывода данных
    def display_data(self):
        print(f"Город: {self.__name}")
        print(f"Регион: {self.__region}")
        print(f"Страна: {self.__country}")
        print(f"Население: {self.__population}")
        print(f"Почтовый индекс: {self.__postal_code}")
        print(f"Телефонный код: {self.__phone_code}")

    # Геттеры и сеттеры
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_region(self):
        return self.__region

    def set_region(self, region):
        self.__region = region

    def get_country(self):
        return self.__country

    def set_country(self, country):
        self.__country = country

    def get_population(self):
        return self.__population

    def set_population(self, population):
        self.__population = population

    def get_postal_code(self):
        return self.__postal_code

    def set_postal_code(self, postal_code):
        self.__postal_code = postal_code

    def get_phone_code(self):
        return self.__phone_code

    def set_phone_code(self, phone_code):
        self.__phone_code = phone_code

# Примеры использования
city = City()
city.input_data()
city.display_data()
city.set_population(1000000)
print(city.get_population())
print()

# Задание 3. Создайте класс «Страна».
# Необходимо хранить в полях класса: название страны, название континента, количество жителей
# в стране, телефонный код страны, название столицы, название городов страны.
# Реализуйте методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным
# полям через методы класса.

print("Задание №3.\n----------------------------------")
class Country:
    def __init__(self, name="", continent="", population=0, phone_code="", capital="", cities=None):
        self.__name = name
        self.__continent = continent
        self.__population = population
        self.__phone_code = phone_code
        self.__capital = capital
        self.__cities = cities if cities is not None else []

    # Методы ввода данных
    def input_data(self):
        self.__name = input("Введите название страны: ")
        self.__continent = input("Введите название континента: ")
        self.__population = int(input("Введите количество жителей: "))
        self.__phone_code = input("Введите телефонный код страны: ")
        self.__capital = input("Введите название столицы: ")
        self.__cities = input("Введите названия городов через запятую: ").split(',')

    # Методы вывода данных
    def display_data(self):
        print(f"Страна: {self.__name}")
        print(f"Континент: {self.__continent}")
        print(f"Население: {self.__population}")
        print(f"Телефонный код: {self.__phone_code}")
        print(f"Столица: {self.__capital}")
        print(f"Города: {', '.join(self.__cities)}")

    # Геттеры и сеттеры
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_continent(self):
        return self.__continent

    def set_continent(self, continent):
        self.__continent = continent

    def get_population(self):
        return self.__population

    def set_population(self, population):
        self.__population = population

    def get_phone_code(self):
        return self.__phone_code

    def set_phone_code(self, phone_code):
        self.__phone_code = phone_code

    def get_capital(self):
        return self.__capital

    def set_capital(self, capital):
        self.__capital = capital

    def get_cities(self):
        return self.__cities

    def set_cities(self, cities):
        self.__cities = cities

    def add_city(self, city):
        self.__cities.append(city)

    def remove_city(self, city):
        if city in self.__cities:
            self.__cities.remove(city)

# Примеры использования
country = Country()
country.input_data()
country.display_data()
country.add_city("Новый город")
print(country.get_cities())
print()

# Задание 4. Создайте класс «Дробь».
# Необходимо хранить в полях класса: числитель и знаменатель. Реализуйте методы класса
# для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса.
# Также создайте методы класса для выполнения арифметических
# операций (сложение, вычитание, умножение, деление, и т.д.).

print("Задание №4.\n----------------------------------")
class Fraction:
    def __init__(self, numerator=0, denominator=1):
        if denominator == 0:
            raise ValueError("Знаменатель не может быть равен нулю")
        self.__numerator = numerator
        self.__denominator = denominator
        self.__simplify()

    # Метод ввода данных
    def input_data(self):
        self.__numerator = int(input("Введите числитель: "))
        denominator = int(input("Введите знаменатель: "))
        if denominator == 0:
            raise ValueError("Знаменатель не может быть равен нулю")
        self.__denominator = denominator
        self.__simplify()

    # Метод вывода данных
    def display_data(self):
        print(f"Дробь: {self.__numerator}/{self.__denominator}")

    # Приватный метод для упрощения дроби
    def __simplify(self):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        common_divisor = gcd(abs(self.__numerator), abs(self.__denominator))
        self.__numerator //= common_divisor
        self.__denominator //= common_divisor

        if self.__denominator < 0:
            self.__numerator *= -1
            self.__denominator *= -1

    # Геттеры и сеттеры
    def get_numerator(self):
        return self.__numerator

    def set_numerator(self, numerator):
        self.__numerator = numerator
        self.__simplify()

    def get_denominator(self):
        return self.__denominator

    def set_denominator(self, denominator):
        if denominator == 0:
            raise ValueError("Знаменатель не может быть равен нулю")
        self.__denominator = denominator
        self.__simplify()

    # Арифметические операции
    def add(self, other):
        new_numerator = self.__numerator * other.__denominator + other.__numerator * self.__denominator
        new_denominator = self.__denominator * other.__denominator
        return Fraction(new_numerator, new_denominator)

    def subtract(self, other):
        new_numerator = self.__numerator * other.__denominator - other.__numerator * self.__denominator
        new_denominator = self.__denominator * other.__denominator
        return Fraction(new_numerator, new_denominator)

    def multiply(self, other):
        new_numerator = self.__numerator * other.__numerator
        new_denominator = self.__denominator * other.__denominator
        return Fraction(new_numerator, new_denominator)

    def divide(self, other):
        if other.__numerator == 0:
            raise ValueError("Нельзя делить на ноль")
        new_numerator = self.__numerator * other.__denominator
        new_denominator = self.__denominator * other.__numerator
        return Fraction(new_numerator, new_denominator)

    # Специальные методы для операторов
    def __add__(self, other):
        return self.add(other)

    def __sub__(self, other):
        return self.subtract(other)

    def __mul__(self, other):
        return self.multiply(other)

    def __truediv__(self, other):
        return self.divide(other)

    def __str__(self):
        return f"{self.__numerator}/{self.__denominator}"

# Примеры использования
f1 = Fraction(1, 2)
f2 = Fraction(3, 4)
print(f1 + f2)  # 5/4
print(f1 - f2)  # -1/4
print(f1 * f2)  # 3/8
print(f1 / f2)  # 2/3
print()
