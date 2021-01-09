# len - длина списка (сколько в нем элементов)
friends = ['Leo', 'Max', 'Kate']

print(len(friends))
print(type(len(friends)))

# .append добавляет новый элемент в список
friends.append('Ron')
print(friends)
print(len(friends))

# .pop() удаляет последний элемент списка и возвращает его
friends.pop()
print(friends)
print(len(friends))
# удаление и вывод
friends.append('Ron')  # добавил снова
print(friends.pop())  # вывел удаленное

# .clear() очищает весь список
friends.clear()
print(len(friends))

# .remove('Ron') - удаление объекта из списка
friends = ['Leo', 'Max', 'Kate', 'Ron']
friends.remove('Ron')
print(friends)

# del friends[0] - удаление элемента по индексу
del friends[2]
print(friends)

#  еще есть сортировка, копирование
#  смотреть в ИДЕ и Гугле

