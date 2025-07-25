# Задание 1. Пользователь вводит с клавиатуры число в диапазоне от 1 до 100.
# Если число кратно 3 (делится на 3 без остатка) нужно вывести слово Fizz.
# Если число кратно 5 нужно вывести слово Buzz. Если число кратно 3 и 5 нужно вывести Fizz Buzz.
# Если число не кратно не 3 и 5 нужно вывести само число.
# Если пользователь ввел значение не в диапазоне от 1 до 100 требуется вывести сообщение об ошибке.

number = float(input("Введите число: "))

if number % 3 == 0 and 1 <= number <= 100:
    print("Fizz")
if number % 5 == 0 and 1 <= number <= 100:
    print("Buzz")
if number % 3 == 0 and number % 5 == 0 and 1 <= number <= 100:
    print("Fizz Buzz")
if number % 3 != 0 and number % 5 != 0 and 1 <= number < 100:
    print(number)
elif number > 100:
    print("Ошибка!")

# Задание 2. Написать программу, которая по выбору пользователя возводит введенное им число в степень
# от нулевой до седьмой включительно.

number = float(input("Введите число: "))
action = float(input("Введите степень: "))

if 0 <= action <= 7:
    print("Возведенное число в степень =", number ** action)
else:
    print("Ошибка!")

# Задание 3. Написать программу подсчета стоимости разговора для разных мобильных операторов.
# Пользователь вводит стоимость разговора и выбирает с какого на какой оператор он звонит. Вывести стоимость на экран.

cost_call = float(input("Введите стоимость разговора: "))
operator = float (input("Введите с какого оператора на какой вы звоните:\n"
                  "MTS - MTS: (Выберите: 1)\n"
                  "MTS - Beeline: (Выберите: 2)\n"
                  "MTS - Megafone: (Выберите: 3)\n"
                  "Beeline - MTS: (Выберите: 4)\n"
                  "Beeline - Beeline: (Выберите: 5)\n"
                  "Beeline - Megafone: (Выберите: 6)\n"
                  "Megafone - MTS: (Выберите: 7)\n"
                  "Megafone - Beeline: (Выберите: 8)\n"
                  "Megafone - Megafone: (Выберите: 9)\n"))

if operator == 1:
    print("Стоимость оператора =", cost_call * 1)
if operator == 2:
    print("Стоимость оператора =", cost_call * 1.1)
if operator == 3:
    print("Стоимость оператора =", cost_call * 1.2)
if operator == 4:
    print("Стоимость оператора =", cost_call * 1.05)
if operator == 5:
    print("Стоимость оператора =", cost_call * 1)
if operator == 6:
    print("Стоимость оператора =", cost_call * 1.15)
if operator == 6:
    print("Стоимость оператора =", cost_call * 1.15)
if operator == 7:
    print("Стоимость оператора =", cost_call * 1.025)
if operator == 8:
    print("Стоимость оператора =", cost_call * 1.23)
if operator == 9:
    print("Стоимость оператора =", cost_call * 1)
if operator > 9:
    print("Ошибка!")

# Задание 4. Зарплата менеджера составляет 200$ + процент от продаж, продажи до 500$—3%, от 500 до 1000—5%,
# свыше 1000 — 8%. Пользователь вводит с клавиатуры уровень продаж для трех менеджеров. Определить их зарплату,
# определить лучшего менеджера, начислить ему премию 200$, вывести итоги на экран.

sales1 = int(input("Введите продажи 1 менеджера (в долларах): "))
sales2 = int(input("Введите продажи 2 менеджера (в долларах): "))
sales3 = int(input("Введите продажи 3 менеджера (в долларах): "))
salary = 200

if sales1 > 1000:
   final_salary1 = salary + sales1 * 0.08
else:
   if sales1 < 500:
       final_salary1 = salary + sales1 * 0.03
   else:
       final_salary1 = salary + sales1 * 0.05

if sales2 > 1000:
   final_salary2 = salary + sales2 * 0.08
else:
   if sales2 < 500:
       final_salary2 = salary + sales2 * 0.03
   else:
       final_salary2 = salary + sales2 * 0.05

if sales3 > 1000:
   final_salary3 = salary + sales3 * 0.08
else:
   if sales3 < 500:
       final_salary3 = salary + sales3 * 0.03
   else:
       final_salary3 = salary + sales3 * 0.05

if final_salary1 > final_salary2 and final_salary1 > final_salary3:
   print("Лучший по продажам - 1 менеджер!")
   final_salary1 += 200

if final_salary2 > final_salary1 and final_salary2 > final_salary3:
   print("Лучший по продажам - 2 менеджер!")
   final_salary2 += 200

if final_salary3 > final_salary1 and final_salary3 > final_salary2:
   print("Лучший по продажам - 3 менеджер!")
   final_salary3 += 200

print("Зарплата 1 менеджера (в долларах) =", final_salary1)
print("Зарплата 2 менеджера (в долларах) =", final_salary2)
print("Зарплата 3 менеджера (в долларах) =", final_salary3)

# Практическое задание на уроке (18.04.2025 - Пятница).
# Задание 1. Пользователь вводит с клавиатуры целое шестизначное число. Написать программу, которая определяет,
# является ли введенное число — счастливым (Счастливым считается шестизначное число, у которого сумма
# первых 3 цифр равна сумме вторых трех цифр). Если пользователь ввел не шестизначное число
# требуется вывести сообщение об ошибке.

number = int(input('Введите шестизначное число: '))
part_1 = number // 1000
a = part_1 // 100
b = (part_1 // 10) % 10
c = part_1 % 10
part_2 = number % 1000
d = part_2 // 100
e = (part_2 // 10) % 10
f = part_2 % 10

if (a + b + c) == (d + e + f):
    print('Счастливое число!')
elif number < 100000:
    print('Введено не шестизначное число. Попробуй еще раз.')
elif number > 999999:
    print('Введено не шестизначное число. Попробуй еще раз.')
else:
    print('Несчастливое число')

# Задание 2. Пользователь вводит шестизначное число. Необходимо поменять в этом числе первую и шестую цифры,
# а так же вторую и пятую цифры. Например, 723895 должно превратиться в 593827.
# Если пользователь ввел не шестизначное число требуется вывести сообщение об ошибке.

number = int(input('Введите шестизначное число: '))
part_1 = number // 1000
a = part_1 // 100
b = (part_1 // 10) % 10
c = part_1 % 10
part_2 = number % 1000
d = part_2 // 100
e = (part_2 // 10) % 10
f = part_2 % 10

if 100000 < number < 999999:
    print('Было ', number, '\nСтало ', f,e,c,d,b,a, sep="")
elif number > 999999:
    print('Введено не шестизначное число. Попробуй еще раз.')
else:
    print('Введено не шестизначное число. Попробуй еще раз.')

# Задание 3. Пользователь вводит с клавиатуры номер месяца (от 1 до 12).
# В зависимости от полученного номера месяца программа выводит на экран надпись:
# Winter (если введено значение 1,2 или 12),
# Spring (если введено значение от 3 до 5),
# Summer (если введено значение от 6 до 8),
# Autumn (если введено значение от 9 до 11).
# Если пользователь ввел значение не в диапазоне от 1 до 12 требуется вывести сообщение об ошибке.

month= int(input('Введите номер месяца от 1 до 12: '))

if month == 1 or month == 2 or month == 12:
    print('Winter')
elif 3 <= month <= 5:
    print('Spring')
elif 6 <= month <= 8:
    print('Summer')
elif 9 <= month <= 11:
    print('Autumn')
else:
    print('В месяце только 12 месяцев. Введи номер месяца от 1 до 12')