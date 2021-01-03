# в блоке else (после while) выполняется действие после того как вышли из цикла while
# т.е. условие цикла while стало неверным (false)

# Вывод чисел от 0 до 100
number = 0
N = int(input('Введи число '))
while number <= N:
    print(number)
    number += 1
    if number == 33:
        break
else:
    print('else finish')

print('standart finish')