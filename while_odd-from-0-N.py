# 1. Вывод четных чисел от 0 до N
number = 0
N = int(input('Введи число '))
while number <= N:
    if number % 2 == 0:
        print(number)
    number += 1
