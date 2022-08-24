#baekjoon 1312


# 구글링을 통해 참고한 풀이
# 초등학교에서 배웠던 나눗셈의 로직으로 풀이가능함.
# 내가 원하는 소숫점 자리가 나올때까지 나눗셈 반복.. 피제수로 제수 나눈 나머지에 10을 곱하고 이를 피제수로 나누어 몫 구하고,,,
# 또 그 나머지에 10 곱하고 다시 피제수로 나누어 몫 구하고..
# 도달점까지 반복하여 구한 몫이 원하는 소수점 자리수의 값.

import sys

a,b,n = map(int, sys.stdin.readline().split())

y = a%b

for _ in range(n):
    res = (y*10)//b
    y = (y*10)%b

print(res)



'''
내 풀이 : 오류는 없어보인다. 소수점 15자리 이상까지 알아낼 수 있다.

a, b, n = map(int, sys.stdin.readline().split())

res = a/b
res = f"{res:.{n+1}f}"
print(res)
res = list(map(str, res))
res.pop()
res = int(res[-1])

if res:
    print(res)

'''

