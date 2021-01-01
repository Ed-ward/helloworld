# математические операции

# средняя продолжительность жизни мужчин в РБ
ale = 64
age = int(input('Сколько Вам лет? '))

# +
after20 = age + 20
print('Через 20 лет Вам будет', after20)

# -
alive = ale - age
print('По статистике Вам осталось прожить', alive)

# *
count = 9485000
all_alive = count * ale
print('Среднее время жизни всех жителей РБ', all_alive, ' лет')

# /  Результат деления всегда float
live_part = age / ale
print('Часть уже прожитой Вами жизни', live_part)
print(type(live_part))


