import sys
n = int(input())
nums = [int(num) for num in input("Nums ").split()]
if (n!=len(nums)):
    print("Incorrect array size!")
    sys.exit()

for i in range(10):
    count = 0
    for num in nums:
        if (num == i):
            count += 1
    print("%s - %s" % (i, (count / len(nums) *100)))