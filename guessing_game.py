# игра угадайка, в уроке она без генератора чисел (((
# сделаем по-нормальному - импортируем модуль рандом
# и запустим с параметром от 1 до 100
import random
number = random.randint(1,100)
print(number)
#number = 43
value = int(input('Введите число от 1 до 100: '))
# 1
if value == number:
    print('Поздравляю, Вы угадали')
else:
    if value < number:
        print('Загаданное число больше чем Ваше.')
        value = int(input('Попробуйте еще раз: '))

    else:
        print('Загаданное число меньше чем Ваше.')
        value = int(input('Попробуйте еще раз: '))

# 2
if value == number:
    print('Поздравляю, Вы угадали')
else:
    if value < number:
        print('Загаданное число больше чем Ваше.')
        value = int(input('Попробуйте еще раз: '))

    else:
        print('Загаданное число меньше чем Ваше.')
        value = int(input('Попробуйте еще раз: '))
# 3
if value == number:
    print('Поздравляю, Вы угадали')
else:
    if value < number:
        print('Загаданное число больше чем Ваше.')
        value = int(input('Попробуйте еще раз: '))

    else:
        print('Загаданное число меньше чем Ваше.')
        value = int(input('Попробуйте еще раз: '))
# 4
if value == number:
    print('Поздравляю, Вы угадали')
else:
    print('Поздравляю, Вы не угадали')