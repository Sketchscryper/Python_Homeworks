# Задание 1. Создайте функцию для отображения текущего времени.
# Функция не принимает параметров. Функция не используя синтаксис декораторов,
# произведите декорирование функции с помощью другой функции.
# Потенциальный вывод данных на экран:
# ***************************
# 23:00
# ***************************
# В этом выводе на экран две линии из звездочек – результаты декорирования.

print("Задание №1.\n-----------------------------")
import datetime

def display_time():
    """Функция для отображения текущего времени"""
    current_time = datetime.datetime.now().strftime("%H:%M")
    print(current_time)

def star_decorator(func):
    """Функция-декоратор, добавляющая рамку из звездочек"""
    def wrapper():
        print("*" * 27)
        func()
        print("*" * 27)
    return wrapper

# Декорирование функции без использования синтаксиса @
decorated_display_time = star_decorator(display_time)

# Вызов декорированной функции
decorated_display_time()
print()

# Задание 2. Добавьте ещё одну функцию для декорирования вывода данных.
# Эта функция должна добавить новые элементы в форматирование вывода.

print("Задание №2.\n-----------------------------")
import datetime

def display_time():
    """Функция для отображения текущего времени"""
    current_time = datetime.datetime.now().strftime("%H:%M")
    print(current_time)

def star_decorator(func):
    """Функция-декоратор, добавляющая рамку из звездочек"""
    def wrapper():
        print("*" * 27)
        func()
        print("*" * 27)
    return wrapper

def dash_decorator(func):
    """Новая функция-декоратор, добавляющая рамку из тире"""
    def wrapper():
        print("-" * 27)
        func()
        print("-" * 27)
    return wrapper

# Декорирование функции без использования синтаксиса @
# Применяем оба декоратора последовательно
decorated_display_time = dash_decorator(star_decorator(display_time))

# Вызов декорированной функции
decorated_display_time()
print()

# Задание 3. Решите задачу из первого задания с использованием синтаксиса декораторов.

print("Задание №3.\n-----------------------------")
import datetime

# Функция-декоратор для добавления рамки из звездочек
def star_decorator(func):
    def wrapper():
        print("*" * 27)
        func()
        print("*" * 27)
    return wrapper

# Функция-декоратор для добавления рамки из тире
def dash_decorator(func):
    def wrapper():
        print("-" * 27)
        func()
        print("-" * 27)
    return wrapper

# Применение декораторов с использованием синтаксиса @
@dash_decorator
@star_decorator
def display_time():
    """Функция для отображения текущего времени"""
    current_time = datetime.datetime.now().strftime("%H:%M")
    print(current_time)

# Вызов декорированной функции
display_time()
print()

# Задание 4. Создайте приложение по выпечке пиццы. Каждая пицца содержит разные компоненты.
# Используя механизм декораторов создайте разные пиццы:
# ■ Маргарита;
# ■ Четыре сыра;
# ■ Капричоза;
# ■ Гавайская.

print("Задание №4.\n-----------------------------")

# Базовый класс пиццы
class Pizza:
    def __init__(self):
        self.ingredients = []
        self.price = 0

    def add_ingredient(self, name, cost):
        """Добавление ингредиента"""
        self.ingredients.append(name)
        self.price += cost

    def __str__(self):
        """Строковое представление пиццы"""
        if not self.ingredients:
            return "Пустая пицца"
        return f"Пицца: {', '.join(self.ingredients)} | Цена: {self.price} руб."

# Декораторы для добавления ингредиентов
def tomato_sauce(func):
    """Добавляет томатный соус"""

    def wrapper():
        pizza = func()
        pizza.add_ingredient("томатный соус", 20)
        return pizza

    return wrapper

def mozzarella(func):
    """Добавляет моцареллу"""

    def wrapper():
        pizza = func()
        pizza.add_ingredient("моцарелла", 50)
        return pizza

    return wrapper

def parmesan(func):
    """Добавляет пармезан"""

    def wrapper():
        pizza = func()
        pizza.add_ingredient("пармезан", 70)
        return pizza

    return wrapper

def gorgonzola(func):
    """Добавляет горгонзолу"""

    def wrapper():
        pizza = func()
        pizza.add_ingredient("горгонзола", 80)
        return pizza

    return wrapper

def emmental(func):
    """Добавляет эмменталь"""

    def wrapper():
        pizza = func()
        pizza.add_ingredient("эмменталь", 60)
        return pizza

    return wrapper

def ham(func):
    """Добавляет ветчину"""

    def wrapper():
        pizza = func()
        pizza.add_ingredient("ветчина", 90)
        return pizza

    return wrapper

def mushrooms(func):
    """Добавляет грибы"""

    def wrapper():
        pizza = func()
        pizza.add_ingredient("грибы", 40)
        return pizza

    return wrapper

def pineapple(func):
    """Добавляет ананас"""

    def wrapper():
        pizza = func()
        pizza.add_ingredient("ананас", 55)
        return pizza

    return wrapper

# Функции для создания разных видов пиццы
@tomato_sauce
@mozzarella
def margherita():
    """Пицца Маргарита"""
    return Pizza()

@mozzarella
@parmesan
@gorgonzola
@emmental
def four_cheeses():
    """Пицца Четыре сыра"""
    return Pizza()

@tomato_sauce
@mozzarella
@ham
@mushrooms
def capricciosa():
    """Пицца Капричоза"""
    return Pizza()

@tomato_sauce
@mozzarella
@ham
@pineapple
def hawaiian():
    """Пицца Гавайская"""
    return Pizza()

# Демонстрация работы
if __name__ == "__main__":
    print("Меню пиццерии:")
    print("1. Маргарита")
    print("2. Четыре сыра")
    print("3. Капричоза")
    print("4. Гавайская")

    choice = input("Выберите пиццу (1-4): ")

    if choice == '1':
        pizza = margherita()
    elif choice == '2':
        pizza = four_cheeses()
    elif choice == '3':
        pizza = capricciosa()
    elif choice == '4':
        pizza = hawaiian()
    else:
        print("Неверный выбор")
        exit()

    print("\nВаша пицца готова!")
    print(pizza)