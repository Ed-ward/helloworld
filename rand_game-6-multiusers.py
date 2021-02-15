# загадываем случайное число. +
import random

number = random.randint(1, 100)
print(number)

# улучшаем цикл (выполняется до равенства чисел)
user_number = None
count = 0
levels = {1: 10, 2: 5, 3: 3}
level = int(input('Введите уровень сложности от 1 до 3: '))
max_count = levels[level]

user_count = int(input('Введите количество игроков: '))
users = []
for i in range(user_count):
    user_name = input(f'Введите имя пользователя {i+1}: ')
    users.append(user_name)

print(users)

is_winner = False
winner_name = None
while not is_winner:
    count += 1
    if count > max_count:
        print('Все игроки проиграли')
        break
    print(f'Попытка № {count}')
    for user in users:
        print(f'Очередь игрока {user}')
        user_number = int(input('Введи число от 1 до 100: '))
        if user_number == number:
            is_winner = True
            winner_name = user
            print(user_number)
            break
        elif number < user_number:
            print('Ваше число больше загаданного!')
        else:
            print('Ваше число меньше загаданного!')
else:
    print(f'Победа! Выиграл {user}!')
