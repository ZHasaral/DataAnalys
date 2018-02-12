mass = [1,2,3,4,5,6,7]

def max(list):
    max = list[0]
    for i in range(len(list)):
      if list[i] > max:
        max = list[i]
    return print(max)


def reverse(list):
    a = int(0)
    n = len(list)
    for i in range(3):
        a = list[i]
        list[i] = list[len(list)-i-1]
        list[len(list)-i -1] = a
    return print(list)


def avg(list):
    sum = int(0)
    for i in range(len(list)):
        sum+=list[i]
    return print(sum/len(list))

max(mass)
reverse(mass)
avg(mass)