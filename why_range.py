# когда полезна функция range

winners = ['Leo', 'Max', 'Kate']

# простой перебор

for winner in winners:
    print(winner)

# что делать если надо вывести место победителя?
# применять while или есть способ лучше?

# вывести нечетные цифры от 1 до 5
# берем список
numbers = [1, 3, 5]
# и перебираем его в цикле for
for number in numbers:
    print(number)
# если цифр много (1000+) ?
# можно юзать while
# но лучше range
