# Задача 2 (Базовая). Тема: Использование стандартных модулей
# Напишите программу, которая:
# Использует модуль random для генерации случайного числа от 1 до 100.
# Выводит текущую дату и время, используя модуль datetime.

# Импортируем необходимые модули
import random
from datetime import datetime

# Генерация случайного числа от 1 до 100
random_number = random.randint(1, 100)
print(f"Случайное число: {random_number}")

# Получение текущей даты и времени
current_datetime = datetime.now()
print(f"Текущая дата и время: {current_datetime}")

# Форматированный вывод даты и времени
formatted_date = current_datetime.strftime("%d.%m.%Y %H:%M:%S")
print(f"Форматированная дата: {formatted_date}")
