# baekjoon 1946(신입사원)

import sys
t = int(sys.stdin.readline())
for _ in range(t):
    count = 0
    n = int(sys.stdin.readline())
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    arr.sort()

    std = arr[0][1]

    for i in arr:
        if i[1] <= std:
            count += 1
            std = i[1]
    
    print(count)




'''

원래 풀이.
풀이의 논리 자체가 잘못되었기 때문에, 몇시간 동안이나 해맸다.
채점기가 코드를 잘못인식하는 것이라 착각했는데
내 풀이가 잘못됐던게 맞다.
내 풀이가 잘못되지 않은 것 같은데 계속 틀리다고 나온다면,
결과가 문제의 조건에 부합하는가에 대해서 계속 검토해보고 나의 풀이논리에 오류가 없었는지 계속 의심해보자.
보통 틀리는 경우.
1. 풀이논리 오류.
2. 풀이의 논리에 맞게 정확히 코딩되지 않음.



t = int(sys.stdin.readline())
for _ in range(t):
    count = 0
    n = int(sys.stdin.readline())
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

    a = min(arr)
    b = min(arr, key=lambda x:x[1])

    a = a[1]
    b = b[0]

    for i in arr:
        if i[1] <= a:
            if i[0] <= b:
                count += 1
            
    print(count)
'''
