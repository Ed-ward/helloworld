# CONTINUE - переход на следующую итерацию цикла,
# команды в цикле после continue не выполняются!

# Вывод четных чисел от 0 до N
number = 0
N = int(input('Введи число '))
while number <= N:
#    number += 1  #если юзаем этот счетчик вместо двух то идет смещение счета.
    if number % 2 != 0:
        number += 1
        continue  # если число соответствует условию то не печатаем его а сразу берем следующее
    print(number)
    number += 1
# пришлось счетчик продублировать, но для примера сойдет
