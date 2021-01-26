# 1: Даны два произвольные списка.
# Удалите из первого списка элементы присутствующие во втором списке.
#  Примечание. Списки создайте вручную, например так:
my_list_1 = [2, 5, 8, 2, 12, 12, 4]
my_list_2 = [2, 7, 12, 3]

# приводим к множеству и вычитаем
my_list_1 = set(my_list_1) - set(my_list_2)
print(my_list_1)

# или так
my_list_1 = [2, 5, 8, 2, 12, 12, 4]
my_list_2 = [2, 7, 12, 3]

for using_value in my_list_2:
    while using_value in my_list_1:
        my_list_1.remove(using_value)
        print(my_list_1)
