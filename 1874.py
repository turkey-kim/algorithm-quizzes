#백준 1874 스택수열.

import sys

arr = []
result = []
stack = []

n = int(sys.stdin.readline())

for i in range(n):
    i = int(sys.stdin.readline())
    arr.append(i)

arrX = list(i for i in range(1,n+1))
arrX.sort(reverse = True)

breakIt = False

for i in range(n): #각 요소들을 하나하나씩 맞추는 반복문.
    while True:
        if stack and stack[-1] == arr[i]:
            break
        if not arrX : # 스택에서 pop할 수 없음에도, 더이상 스택에 푸쉬할 요소가 남아있지 않을 때.
            breakIt = True
            break
        
        x= arrX.pop()
        stack.append(x)
        result.append('+')
        
    if breakIt:
        break
    
    x= stack.pop()
    result.append('-')


if breakIt:
    print('NO')
else:
    for i in result:
        print(i)
