# Задание 1. Создайте класс очереди для работы с символьными значениями.
# Требуется создать реализации для операций над элементами:
# ■ IsEmpty — проверка очереди на пустоту.
# ■ IsFull — проверка очереди на заполнение.
# ■ Enqueue — добавление элемента в очередь.
# ■ Dequeue — удаление элемента из очереди.
# ■ Show — отображение всех элементов очереди на экран.
# При старте приложения нужно отобразить меню с помощью, которого пользователь
# может выбрать необходимую операцию.

print("Задание №1.\n------------------------------------")
class Queue:
    def __init__(self, size):
        """
        Инициализация очереди с заданным размером.

        :param size: максимальный размер очереди
        """
        self.size = size
        self.data = [None] * size
        self.front = 0  # указатель на начало очереди
        self.rear = -1  # указатель на конец очереди
        self.count = 0  # количество элементов в очереди

    def IsEmpty(self):
        """Проверка очереди на пустоту."""
        return self.count == 0

    def IsFull(self):
        """Проверка очереди на заполнение."""
        return self.count == self.size

    def Enqueue(self, value):
        """
        Добавление элемента в очередь.

        :param value: символ для добавления
        :raises OverflowError: если очередь заполнена
        """
        if self.IsFull():
            raise OverflowError("Очередь заполнена")
        self.rear = (self.rear + 1) % self.size
        self.data[self.rear] = value
        self.count += 1

    def Dequeue(self):
        """
        Удаление элемента из очереди.

        :return: удаленный элемент
        :raises IndexError: если очередь пуста
        """
        if self.IsEmpty():
            raise IndexError("Очередь пуста")
        value = self.data[self.front]
        self.front = (self.front + 1) % self.size
        self.count -= 1
        return value

    def Show(self):
        """Отображение всех элементов очереди."""
        if self.IsEmpty():
            print("Очередь пуста")
            return

        elements = []
        index = self.front
        for _ in range(self.count):
            elements.append(self.data[index])
            index = (index + 1) % self.size
        print("Элементы очереди:", ' '.join(elements))

def main():
    queue_size = int(input("Введите размер очереди: "))
    q = Queue(queue_size)

    while True:
        print("\nМеню:")
        print("1. Проверить, пуста ли очередь (IsEmpty)")
        print("2. Проверить, заполнена ли очередь (IsFull)")
        print("3. Добавить элемент (Enqueue)")
        print("4. Удалить элемент (Dequeue)")
        print("5. Показать очередь (Show)")
        print("6. Выход")

        choice = input("Выберите операцию: ")

        if choice == '1':
            print("Очередь пуста?", q.IsEmpty())

        elif choice == '2':
            print("Очередь заполнена?", q.IsFull())

        elif choice == '3':
            value = input("Введите символ для добавления: ")
            try:
                q.Enqueue(value)
                print(f"Элемент '{value}' добавлен в очередь.")
            except OverflowError as e:
                print("Ошибка:", e)

        elif choice == '4':
            try:
                removed = q.Dequeue()
                print(f"Удален элемент '{removed}'")
            except IndexError as e:
                print("Ошибка:", e)

        elif choice == '5':
            q.Show()

        elif choice == '6':
            print("Программа завершена.")
            break

        else:
            print("Неверный выбор. Попробуйте еще раз.")

if __name__ == "__main__":
    main()
print()

# Задание 2. Создайте класс очереди с приоритетами для работы с символьными значениями.
# Требуется создать реализации для операций над элементами очереди:
# ■ IsEmpty — проверка очереди на пустоту.
# ■ IsFull — проверка очереди на заполнение.
# ■ InsertWithPriority — добавление элемента c приоритетом в очередь.
# ■ PullHighestPriorityElement - удаление элемента с самым высоким приоритетом из очереди.
# ■ Peek — возврат самого большого по приоритету элемента.
# Обращаем ваше внимание, что элемент не удаляется из очереди.
# ■ Show — отображение всех элементов очереди на экран.
# При показе элемента также необходимо отображать приоритет.
# При старте приложения нужно отобразить меню с помощью, которого пользователь
# может выбрать необходимую операцию.

print("Задание №2.\n------------------------------------")
class PriorityQueue:
    def __init__(self, max_size):
        """Инициализация очереди с заданным максимальным размером"""
        self.max_size = max_size
        self.queue = []

    def is_empty(self):
        """Проверка очереди на пустоту"""
        return len(self.queue) == 0

    def is_full(self):
        """Проверка очереди на заполнение"""
        return len(self.queue) == self.max_size

    def insert_with_priority(self, value, priority):
        """Добавление элемента с приоритетом в очередь"""
        if self.is_full():
            print("Очередь заполнена. Невозможно добавить элемент.")
            return

        # Добавляем элемент как кортеж (приоритет, значение)
        self.queue.append((priority, value))
        # Сортируем очередь по убыванию приоритета
        self.queue.sort(reverse=True, key=lambda x: x[0])
        print(f"Элемент '{value}' с приоритетом {priority} добавлен в очередь.")

    def pull_highest_priority_element(self):
        """Удаление элемента с самым высоким приоритетом"""
        if self.is_empty():
            print("Очередь пуста. Невозможно извлечь элемент.")
            return None

        # Извлекаем элемент с наивысшим приоритетом (первый в списке)
        priority, value = self.queue.pop(0)
        print(f"Элемент '{value}' с приоритетом {priority} извлечен из очереди.")
        return value

    def peek(self):
        """Возврат самого большого по приоритету элемента без удаления"""
        if self.is_empty():
            print("Очередь пуста.")
            return None

        priority, value = self.queue[0]
        print(f"Элемент с наивысшим приоритетом: '{value}', приоритет: {priority}")
        return value

    def show(self):
        """Отображение всех элементов очереди с их приоритетами"""
        if self.is_empty():
            print("Очередь пуста.")
            return

        print("Элементы очереди (значение: приоритет):")
        for priority, value in self.queue:
            print(f"'{value}': {priority}")

# Функция для отображения меню
def display_menu():
    print("\nМеню операций с очередью с приоритетами:")
    print("1. Проверить пуста ли очередь")
    print("2. Проверить заполнена ли очередь")
    print("3. Добавить элемент с приоритетом")
    print("4. Извлечь элемент с наивысшим приоритетом")
    print("5. Просмотреть элемент с наивысшим приоритетом")
    print("6. Показать все элементы очереди")
    print("7. Выход")

# Основная функция программы
def main():
    max_size = int(input("Введите максимальный размер очереди: "))
    queue = PriorityQueue(max_size)

    while True:
        display_menu()
        choice = input("Выберите операцию (1-7): ")

        if choice == '1':
            if queue.is_empty():
                print("Очередь пуста.")
            else:
                print("Очередь не пуста.")

        elif choice == '2':
            if queue.is_full():
                print("Очередь заполнена.")
            else:
                print("Очередь не заполнена.")

        elif choice == '3':
            if queue.is_full():
                print("Очередь заполнена. Невозможно добавить элемент.")
            else:
                value = input("Введите символьное значение: ")
                priority = int(input("Введите приоритет (целое число): "))
                queue.insert_with_priority(value, priority)

        elif choice == '4':
            queue.pull_highest_priority_element()

        elif choice == '5':
            queue.peek()

        elif choice == '6':
            queue.show()

        elif choice == '7':
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор. Пожалуйста, выберите от 1 до 7.")

if __name__ == "__main__":
    main()
print()

# Задание 3. Необходимо разработать приложение, которое позволит сохранять информацию о
# логинах пользователей и их паролях. Каждому пользователю соответствует пара логин-пароль.
# ■ Добавить нового пользователя
# ■ Удалить существующего пользователя
# ■ Проверить существует ли пользователь
# ■ Изменить логин существующего пользователя
# ■ Изменить пароль существующего пользователя
# Для реализации задания обязательно используйте одну из структур данных.
# При выборе руководствуйтесь постановкой задачи.

print("Задание №3.\n------------------------------------")
class UserManager:
    def __init__(self):
        """Инициализация менеджера пользователей"""
        self.users = {}  # Словарь для хранения пользователей (логин: пароль)

    def add_user(self, login, password):
        """Добавление нового пользователя"""
        if login in self.users:
            print(f"Пользователь с логином '{login}' уже существует!")
            return False
        self.users[login] = password
        print(f"Пользователь '{login}' успешно добавлен.")
        return True

    def remove_user(self, login):
        """Удаление существующего пользователя"""
        if login not in self.users:
            print(f"Пользователь с логином '{login}' не найден!")
            return False
        del self.users[login]
        print(f"Пользователь '{login}' успешно удален.")
        return True

    def user_exists(self, login):
        """Проверка существования пользователя"""
        exists = login in self.users
        print(f"Пользователь '{login}' {'' if exists else 'не '}существует.")
        return exists

    def change_login(self, old_login, new_login):
        """Изменение логина пользователя"""
        if old_login not in self.users:
            print(f"Пользователь с логином '{old_login}' не найден!")
            return False
        if new_login in self.users:
            print(f"Логин '{new_login}' уже занят!")
            return False

        password = self.users[old_login]
        del self.users[old_login]
        self.users[new_login] = password
        print(f"Логин изменен с '{old_login}' на '{new_login}'.")
        return True

    def change_password(self, login, new_password):
        """Изменение пароля пользователя"""
        if login not in self.users:
            print(f"Пользователь с логином '{login}' не найден!")
            return False

        self.users[login] = new_password
        print(f"Пароль для пользователя '{login}' успешно изменен.")
        return True

    def show_users(self):
        """Отображение списка пользователей"""
        if not self.users:
            print("Нет зарегистрированных пользователей.")
            return

        print("Список пользователей:")
        for i, (login, password) in enumerate(self.users.items(), 1):
            print(f"{i}. Логин: {login}, Пароль: {'*' * len(password)}")

# Функция для отображения меню
def display_menu():
    print("\nМеню управления пользователями:")
    print("1. Добавить нового пользователя")
    print("2. Удалить пользователя")
    print("3. Проверить существование пользователя")
    print("4. Изменить логин пользователя")
    print("5. Изменить пароль пользователя")
    print("6. Показать всех пользователей")
    print("7. Выход")

# Основная функция программы
def main():
    user_manager = UserManager()

    while True:
        display_menu()
        choice = input("Выберите операцию (1-7): ")

        if choice == '1':
            login = input("Введите логин нового пользователя: ")
            password = input("Введите пароль: ")
            user_manager.add_user(login, password)

        elif choice == '2':
            login = input("Введите логин пользователя для удаления: ")
            user_manager.remove_user(login)

        elif choice == '3':
            login = input("Введите логин пользователя для проверки: ")
            user_manager.user_exists(login)

        elif choice == '4':
            old_login = input("Введите текущий логин пользователя: ")
            new_login = input("Введите новый логин: ")
            user_manager.change_login(old_login, new_login)

        elif choice == '5':
            login = input("Введите логин пользователя: ")
            new_password = input("Введите новый пароль: ")
            user_manager.change_password(login, new_password)

        elif choice == '6':
            user_manager.show_users()

        elif choice == '7':
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор. Пожалуйста, выберите от 1 до 7.")

if __name__ == "__main__":
    main()