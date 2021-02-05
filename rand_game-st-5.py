# загадываем случайное число. +
import random

number = random.randint(1, 100)
print(number)

# улучшаем цикл (выполняется до равенства чисел)
user_number = None
while number != user_number:
    user_number = int(input('Введи число от 1 до 100: '))
    print(user_number)

    if number < user_number:
        print('Ваше число больше загаданного!')
    elif number > user_number:
        print('Ваше число меньше загаданного!')

print('Победа! Вы угадали!')
