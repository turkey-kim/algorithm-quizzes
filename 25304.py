# baekjoon 25304

import sys

x = int(sys.stdin.readline())
n = int(sys.stdin.readline())
cnt = 0
for _ in range(n):
    a,b = map(int, sys.stdin.readline().split())
    cnt += (a*b)

if x == cnt:
    print('Yes')
else:
    print('No')
