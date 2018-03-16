list = []
for i in range(int(input())):
    list.append(int(input()))
print(list)

def avg(list):
    sum = float(0)
    for i in range(len(list)):
        sum+=list[i]
    return(sum/len(list))

print("Cреднее значение равно",avg(list))


def median(list):
    n = len(list)
    if n % 2 == 1:
            return(list[n//2])
    else:
            return(sum(list[n//2-1:n//2+1])/2.0)

print("Медиана равна",median(list))


print("Сумма среднего значения и медианы ",median(list)+avg(list))