# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

sum = int(input("Sum: "))
prod = int(input("Product: "))

num1 = None
num2 = None

for i in range(sum):
    for j in range(sum):
        if i + j == sum and i * j == prod:
            num1 = i
            num2 = j

print(num1, num2)