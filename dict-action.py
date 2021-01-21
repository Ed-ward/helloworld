# основные действия со словарем

# получение элемента по ключу
# friend['name']
friend = {
    'name': 'Max',
    'age': 23
}
print(friend)
print(type(friend))
print(friend['age'])

# добавление значения
friend['has_car'] = True
print(friend)

# изменение значения
friend['has_car'] = False
print(friend)

# удаление значения
del friend ['age']
print(friend)

# оператор in - проверить есть ли ключ в словаре
if 'age' in friend:
    print('Есть возраст в словаре')
else: print('В словаре нет возраста')

if 'has_car' in friend:
    print('Есть машина в словаре')
else: print('В словаре нет машины')

