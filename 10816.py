# baekjoon 10816

import sys
sys.setrecursionlimit(2500)

N = int(sys.stdin.readline())
n = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
m = list(map(int, sys.stdin.readline().split()))
n.sort()

def bs(i,start,end):
    while start <= end:
        mid = (start+end)//2
        if i == n[mid]:
            start = mid
            end = mid
            while (n[start] == i) or (n[end] == i) or not n[start] or not n[end]:
                if n[start] == i:
                    start -= 1
                elif n[end] == i:
                    end += 1
            start += 1
            end -= 1
            return (end-start+1)
                    
                             
        elif i < n[mid]:
            end = mid - 1
        else:
            start = mid + 1

            
        if start > end:
            return 0
           
for i in m:
    start = 0
    end = len(n)-1
    print(bs(i,start,end), end=' ')

# 결과는 나오지만, 시간초과.
# 6 3 2 10 10 10 -10 -10 7 3
# 10 9 -5 2 3 4 5 -10
