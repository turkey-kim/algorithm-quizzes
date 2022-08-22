# 백준 1546(1차원 배열)

import sys

t = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))
M = max(arr)
res =[]

for i in arr:
    i = (i/M)*100
    res.append(i)

result = sum(res)/t

print(result)
    
    
