friends = 'Максим Леонид'
print(friends)

# len - определение длины строки - len(friend)
print(len(friends))

# find - ищет заданный символ в строке - friend.find('а')
print(friends.find('Лео'))  # вернет 7 - номер начального символа.
print(friends.find('123Лео'))  # если то что ищем не существует то вернется -1

# split - разбиение строки - friend.split()
# без параметра разбивает строку по пробелам и выдает список,
print(friends.split())  # вот такой ['Максим', 'Леонид']
friend = 'Максим;Леонид'
print(friend.split(';'))

# isdigit - проверяет состоит ли строка только из чисел friend.isdigit()
print(friends.isdigit())  # возвращает True или False
numbers = '123456789'
print(numbers.isdigit())

# upper - приведение строки к верхнему регистру friend.upper()
print(friend.upper())

# lower - приведение строки к нижнему регистру. friend.lower()
print(friend.lower())


