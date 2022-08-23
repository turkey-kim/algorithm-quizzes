# beckjoon 2217

import sys

n = int(sys.stdin.readline())
arr = []
res = []

for _ in range(n):
    r = int(sys.stdin.readline())
    arr.append(r)

arr.sort()
l = len(arr)

for i in arr:
    i *= l
    res.append(i)
    l -= 1

print(max(res)) #답 ; 부르트포스로 실행한 결과값 전부다 res에 넣었다.

