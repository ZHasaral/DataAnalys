#Вычислите N! ("эн-факториал") – произведение всех натуральных чисел от 1 до N ( N!=1∙2∙3∙…∙ N ).
s = 1
n = int(input())
for i in range(2, n+1):
    s = s * i
print(s)