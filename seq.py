# последовательность - контейнер, элементы к-рой
# представляют собой последовательность.

# типы данных строка список и кортеж - последовательности,
# для них можно прменять одинаковые функциии.
friend_name = 'Max'
friends = ['Max', 'Leo', 'Kate']
roles = ('admin', 'guest', 'user')

# типы данных
print(type(friend_name))
print(type(friends))
print(type(roles))

# индексация
print(friend_name[1])
print(friends[1])
print(roles[1])

# срезы
print(friend_name[1:])
print(friends[1:])
print(roles[1:])

# длина
print(len(friend_name))
print(len(friends))
print(len(roles))
