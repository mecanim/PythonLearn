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