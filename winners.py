# введение
print('Здравствуйте! Вас приветствует программа "Winners(R)"')
print('Соревнования по Python')

# уточняем сколько нас
count = int(input('Введите количество участников: '))
# приготовим список
members = []

# count будет счетчиком в цикле
i = count

while i > 0:
     name = input('Кто занял {} место? ' .format(i))
     members.append(name)
     i -=1

# кто участвовал + сортировка
# применится только к этому выводу, сам список не перемешается
print('В соревнованиях участвовали: ', sorted(members))

# делаем переворот списка так как люди записаны с конца
members.reverse()

# достаем из списка первые три места срезом от 0 до 3х
result = members[:3]

result = 'Победители: {}. Поздравляем!' .format(result)
print(result)