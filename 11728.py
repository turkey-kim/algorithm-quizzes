# baekjoon 11728

import sys

n, m =map(int, sys.stdin.readline().split())


A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

c = A+B
c.sort()

for i in c:
    print(i, end=' ')
