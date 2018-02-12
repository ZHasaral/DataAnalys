list = []
flag = int(1)
n = int(input())
for i in range(n):
    tmp = []
    for j in range(n):
        x = int(input())
        tmp.append(x)
    list.append(tmp)


for i in range(len(list)):
    for j in range(len(list)):
        if i!=j and list[i][j] != list[j][i]:
            flag = 0
if flag == 0:
    print("no")
else:
    print("yes")


def printM(a):
    for i in range(len(a)):
        print(a[i])
printM(list)