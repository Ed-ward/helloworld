# приведение типов
# число к строке str(number)
# строка к числу int(word) и т.д.

birthday_year = '1988'
print(type(birthday_year))
# <class 'str'> ! надо преобразовать в число

birthday_year = int(birthday_year)
print(type(birthday_year))
# <class 'int'> сделал отдельно,
# но лучше было бы сразу в age привести к числовому

period = 20
print(type(period))
# <class 'int'>

age = birthday_year + period
print(age)

# а это число в строку, а потом контантенация
text = 'он родился в '
number = 1989
text_plus_number = text + str(number)
print(text_plus_number)