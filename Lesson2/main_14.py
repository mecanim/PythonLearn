#Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

num = int(input("Num: "))
pow = 0
PowedNum = 2 ** pow

while PowedNum <= num:
    print(PowedNum)
    pow += 1
    PowedNum = 2 ** pow

