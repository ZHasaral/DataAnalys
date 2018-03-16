#Выведите все элементы списка с четными индексами (то есть A[0], A[2], A[4], ...).
num = input()
a = [int(i) for i in str(num)]
for i in range(0,len(a), 1):
  if i%2 == 0:
    print(a[i])