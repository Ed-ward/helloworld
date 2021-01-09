# Форматирование строк

name = 'Leo'
age = 30

# 1 конкатенация "+" не рекомендуется
hello_str = 'Привет, ' + name + '. Тебе ' + str(age) + ' лет.'
print(hello_str)

# 2 %
hello_str = 'Привет, %s. Тебе %d лет.' %(name, age)  # %s - строка  %d - число
print(hello_str)


# 3 format рекомендуется
hello_str = 'Привет, {}. Тебе {} лет.' .format(name, age)
print(hello_str)

