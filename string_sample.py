# объявление переменной строкового типа:
friend = 'Максим'
# или так
amigo = "Саша"
# проверим
print(friend)
print(type(friend))
print(amigo)
print(type(amigo))

# Если в строке нужны кавычки то надо использовать кавычки разных типов
say = 'say "Hello"'
print(say)
say = "say 'Hello'"
print(say)

# строка состоит из символов,
# можно получить символ по номеру в строке
# friend[1]
# счет индексов идет с 0

first_letter = friend[0]
print('Первая буква имени друга: ', first_letter)
print("Тип первого символа тоже строка: ", type(first_letter))

# можно использовать отрицательные индесы
# для получения символа отсчитывая с конца строки
# friend[-3]

last_letter = friend[-1]
print('Последняя буква имени друга: ', last_letter)

no_last_letter = friend[-2]
print('Предпоследняя буква имени друга: ', no_last_letter)
