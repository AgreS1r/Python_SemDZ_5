# Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.

def power(A, B):
    if B == 0:
        return 1
    elif B % 2 == 0:
        return power(A, B // 2) ** 2
    else:
        return A * power(A, B - 1)

a = int(input("Введите число A: "))
b = int(input("Введите степень B: "))
result = power(a, b)
print(f"{a} в степени {b} = {result}")

# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

def sum(a, b):
    if b == 0:
        return a
    elif a == 0:
        return b
    else:
        return sum(a + 1, b - 1)

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
result = sum(a, b)
print(f"Сумма чисел {a} и {b} равна {result}.")