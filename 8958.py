# beckjoon 8958

import sys

t = int(sys.stdin.readline())
result = []
for _ in range(t):
    arr = list(map(str, sys.stdin.readline()))
    arr.pop()
    res = []
    count = 0

    for i in arr:
        if i =='O':
            count += 1
            res.append(count)
        elif i == 'X':
            count = 0
    result.append(sum(res))

for i in result:
    print(i)
    
