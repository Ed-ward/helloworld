# действия со множествами

# добавление элемента cities.add('Burma')
cities = {'Las Vegas', 'Paris', 'Moscow'}
print(cities)
cities.add('Burma')
print(cities)
cities.add('Moscow')
print(cities)

# удаление элемента cities.remove('Moscow')
cities.remove('Moscow')
print(cities)

# длина множества len
print(len(cities))

# оператор in
print('Paris' in cities)

# цикл for
for city in cities:
    print(city)
