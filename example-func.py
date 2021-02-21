# пользователь вводит три числа
# надо отобразить минимальное максимальное и сумму,

# делаем пустой список
numbers = []

# разрешаем ввести число три раза
for i in range(3):
    number = int(input('введите число '))
    numbers.append(number)

print(max(numbers))
print(min(numbers))
print(sum(numbers))



