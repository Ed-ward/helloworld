# Практическое задание
# 2: Используя цикл, запрашивайте у пользователя число,
# пока оно не станет больше 0, но меньше 10.
# После того, как пользователь введет корректное число,
# возведите его в степень 2 и выведите на экран.

# Например, пользователь вводит число 123, вы сообщаете ему,
# что число неверное, и говорите о диапазоне допустимых. И просите ввести заново.
# Допустим, пользователь ввел 2, оно подходит. Возводим его в степень 2 и выводим 4.

# print('Введи число от 0 до 10')

# number = 100 убрал предварительное значение чтобы  иде не ругалась на переопределение переменной
# код получился короче и проще чем у преподавателя

number = int(input('Введи число от 0 до 10  '))

while number < 0 or number > 10:
    number = int(input('Это число не подходит. Введи число от 0 до 10 '))
else:
    print(number ** 2)
