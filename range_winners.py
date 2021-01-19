winners = ['Leo', 'Max', 'Kate']

# используем  range
for i in range(len(winners)):
#    print(i)
#    print(winners[i])
# удобнее чем  while

    print(i+1, ')', winners[i])

# upd
# применение range с параметрами

for i in range(1, len(winners)+1):
    print(i, ')', winners[i-1])
# ничего особо не улучшилось, зато есть альтернатива :)
