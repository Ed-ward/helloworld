# 1 загадываем случайное число. +
import random

number = random.randint(1, 100)
print(number)

# 2 пользователь вводит число

# user_number = int(input('Введи чило от 1 до 100: '))
# print(user_number)

# 3 сравнить числа

# if number == user_number:
#     print('Вы угадали!')
# elif number < user_number:
#     print('Ваше число больше загаданного!')
# else:
#     print('Ваше число меньше загаданного!')

# 4 сделать цикл

while True:
    user_number = int(input('Введи чило от 1 до 100: '))
    print(user_number)
    if number == user_number:
        print('Вы угадали!')
        break
    elif number < user_number:
        print('Ваше число больше загаданного!')
    else:
        print('Ваше число меньше загаданного!')
