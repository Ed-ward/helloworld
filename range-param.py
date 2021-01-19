# параметры range

# range(start_or_stop, stop[, step])  где

# start_or_stop - начало или конец последовательности

# stop - конец

# step - шаг


# Пример - вывести четные цифры от 1 до 5
numbers = [1, 3, 5]
for number in numbers:
    print(number)

print(list(range(1, 1000, 2)))

# то же самое в цикле for:
for number in range(1, 1000, 2):
    print(number)

# for - перебор последовательности, индекс не нужен

# for range - перебор последовательности, нужен индекс
# for range можно использовать чтобы пропускать элементы (шаг)
# или идти с конца в начало

# while - цикл связан с условием, но не с последовательностью.

