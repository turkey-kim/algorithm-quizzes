# 백준 4673

import sys

arr = []

for i in range(1,10001):
    x = list(map(str, str(i)))
    x = sum(map(int,x))
    i += x
    arr.append(i)
        

for i in range(1,10001):
    if i not in arr:
        print(i)    

