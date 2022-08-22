#beckjoon 4344

import sys

t = int(sys.stdin.readline())
result = []

for _ in range(t):
    arr = list(map(int, sys.stdin.readline().split()))
    average = (sum(arr)-arr[0])/arr[0]
    count = 0
    for i in arr[1:]:
        if i > average:
            count+=1

    res = (count/arr[0])*100
    res = format(res, ".3f")
    result.append(res)
    
    
for i in result:
    print(f'{i}%')

# format()함수를 쓰면 원하는 소숫점 자리수까지 표시할 수 있다.
