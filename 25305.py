#백준 25305번(정렬)

import sys

n, k =map(int, sys.stdin.readline().split())
N = list(map(int, sys.stdin.readline().split()))
N.sort(reverse= True)
print(N[k-1])
         
