from random import randint
from datetime import datetime

n = 10000000000000
num = randint(1, n)
print(num)
low = 0
high = n - 1
r = 0
# for i in range(1,n):
# if num == i:
# print(i)
# break
start = datetime.now()
while low <= high:
    middle = (low + high) // 2
    if middle == num:
        print(middle)
        break
    elif middle > num:
        high = middle - 1
    else:
        low = middle + 1
    r += 1
print(r)
end = datetime.now()
print(end - start)
