# Задача 5 (Продвинутая). Тема: Установка и использование внешних пакетов.
# Установите библиотеку requests через pip.
# Напишите скрипт, который отправляет GET-запрос на сайт https://jsonplaceholder.typicode.com/posts/1.
# Распечатайте статус-код ответа и содержимое в формате JSON.

import requests

def fetch_data():
    # URL для запроса
    url = "https://jsonplaceholder.typicode.com/posts/1"

    try:
        # Отправляем GET-запрос
        response = requests.get(url)

        # Проверяем статус-код
        print(f"Статус-код: {response.status_code}")

        # Проверяем успешность запроса
        if response.status_code == 200:
            # Парсим JSON-ответ
            data = response.json()
            print("Содержимое ответа:")
            print(data)
        else:
            print("Ошибка при выполнении запроса")

    except requests.exceptions.RequestException as e:
        # Обработка ошибок
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    fetch_data()
