#baekjoon 2309

import sys

arr = []
breaker = False

for i in range(9):
    i = int(sys.stdin.readline())
    arr.append(i)

for x in arr:
    for y in arr:
        res = []
        for z in arr:
            if x==y or z==x or z==y:
                continue
            else:
                res.append(z)
        if sum(res) == 100:
            breaker = True
            break
    if breaker:
        break

res.sort()
for i in res:
    print(i)
            

