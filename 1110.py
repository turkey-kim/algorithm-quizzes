#baekjoon 1110

import sys

n = int(sys.stdin.readline())

if n < 10:
    n = [ '0', str(n) ]
else:
    n = list(map(str, str(n)))
    
arr = n
res = arr[0]+arr[1]
x = '10000'
cnt = 0


while x != res:
    cnt += 1
    if int(x) >= 10:
        a, b = map(int, n)
        x = a+b
        x = x%10
        n[0] = str(b)
        n[1] =str(x)
        x = str(b) + str(x)
    elif 0 < int(x) < 10:
        x = int(x)
        n[0] = str(x)
        n[1] =str(x)
        x = str(x) + str(x)           
        

print(cnt)

# 쓰잘대기없이 길게 풀었다. https://wook-2124.tistory.com/222
# 숫자형을 자료형으로 불필요하게 바꾸려다보니 이렇게 됐다.
# 내가 생각하는 풀이보다 더 괜찮은 풀이가 있나 계속 생각해봐야한다.
