friend = {
    'name': 'Max',
    'age': 23,
    'has_car': True
}
print('варианты перебора словаря')

print('по ключам')
for key in friend.keys():
    print(key)   # получаем только ключи
    print(friend[key])  # получаем и значения

print('тоже самое')
for key in friend:
    print(key)  # получаем только ключи
    print(friend[key])  # получаем ключи и значения


print('по значениям!')
for val in friend.values():
    print(val)


print('по парам ключ-значение')
for item in friend.items():   # перебираем пары в виде кортежа
    print(item)

print('более удобный способ: в одну переменную - ключ, во вторую - значение')
for key, val in friend.items():
    print(key)
    print(val)
