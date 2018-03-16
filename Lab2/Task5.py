#Необходимо вывести  сумму цифр числа N
n = int(input())
e = int(0)

while n > 0:
    e+=n%10
    n/=10
print(e)
