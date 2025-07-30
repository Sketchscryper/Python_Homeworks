# Задача 3 (Средняя). Тема: Создание своего пакета
# Создайте структуру пакета:
# my_package/
#     __init__.py
#     calculator.py
#     greeting.py
# В calculator.py определите функции add(a, b) и multiply(a, b).
# В greeting.py определите функцию say_hello(name).
# В файле вне пакета (main.py) импортируйте обе функции и используйте их.

from my_package.calculator import add, multiply
from my_package.greeting import say_hello

# Использование функций
result_add = add(7, 3)
result_multiply = multiply(5, 6)
greeting = say_hello("Андрей")

print(f"Сумма: {result_add}")
print(f"Произведение: {result_multiply}")
print(greeting)