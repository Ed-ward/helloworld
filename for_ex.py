# с последовательностями нормально юзаются циклы for

friend_name = 'Max'
friends = ['Max', 'Leo', 'Kate']
roles = ('admin', 'guest', 'user')

# проверки на соответствие in тоже кул
if 'Max' in friends:
    print('У меня уже есть этот амиго')

if 'M' in friend_name:
    print('Буква "М" есть в имени друга')

# while
i = 0
while i < len(friends):
    friend = friends[i]
    i += 1
    print(friend)

# для for не нужен счетчик!
# Цикл FOR позволяет перебирать элементы последовательности
# по порядку без указания индекса
# Заканчивается выполнение цикла когда заканчивается последовательность
# это позволяет совершать меньше ошибок при переборе элементов
for friend in friends:
    print(friend)


# for для строки
for letter in friend_name:
    print(letter)

# for для кортежа
for role in roles:
    print(role)

# для перебора предпочтительно for a нe while!
