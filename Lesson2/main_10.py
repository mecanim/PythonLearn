# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, 
# которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть

n = int(input("Coins number: "))

obverseNum = 0
reverseNum = 0

for i in range(n):
    x = int(input("obv.: 1, rev.: 0. Enter: "))
    if x == 1:
        obverseNum += 1
    else:
        reverseNum += 1

print(min(obverseNum, reverseNum))