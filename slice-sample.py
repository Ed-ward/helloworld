# срезы дают возможность поучить несколько символов из строки
# friend[start:end]
# friend[1:4]
# 1 - какого символа, 4 - по какой символ
# friend[:4] - срез с начала строки
# friend[1:] - срез до конца строки

friend = 'Максим'

print(friend[1:4])
print(friend[:4])
print(friend[3:])
print(type(friend[1:4]))
