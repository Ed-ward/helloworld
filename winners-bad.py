print('Здравствуйте! Вас приветствует программа "Winners(R)"')
name5 = input('Кто занял 5-е место? ')
name4 = input('Кто занял 4-е место? ')
name3 = input('Кто занял 3-е место? ')
name2 = input('Кто занял 2-е место? ')
name1 = input('Кто занял 1-е место? ')

congrats = "В соревнованиях участвовали: [ '{}', '{}', '{}', '{}', '{}']" .format(name5, name4, name3, name2, name1)
print(congrats)

congrats = 'Победители: {} {} {}. Поздравляем!'.format(name1, name2, name3)
print(congrats)
