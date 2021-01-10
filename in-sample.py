friends = ['Leo', 'Max', 'Kate', 'Ron']

# Оператор in - проверяет наличие элемента в списке
print('Max' in friends)
# in работает и со строками - проверяет есть ли в них символ
print('S' in 'Spiderman')

# ну или так можно проверить есть ли что-то в string
hero = 'Superman'
if hero.find('man') != -1:
    print('Yes')

if 'man' in hero:
    print('Yes')

# a так можно проверить есть ли что-то в list

goals = ['стать гуру', 'здоровье', 'накормить кота']
if 'здоровье' in goals:
    print('all right')
