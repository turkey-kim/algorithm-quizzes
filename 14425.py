#baekjoon 14425

import sys

n,m = map(int, sys.stdin.readline().split())
s= []
M= []
cnt = 0

for i in range(n):
    i = sys.stdin.readline()
    s.append(i)
    
set(s)


for i in range(m):
    i = sys.stdin.readline()
    M.append(i)
    if i in s:
        cnt += 1

print(cnt)



'''
원래 풀이 :

import sys

n,m = map(int, sys.stdin.readline().split())
s= []
M= []
count = 0

for i in range(n):
    i = sys.stdin.readline()
    s.append(i)
    
for i in range(m):
    i = sys.stdin.readline()
    M.append(i)

for x in s:
    for y in M:
        if x == y:
            count += 1

print(count)


-> 시간초과로 오답처리.
-> 꼭 이중 반복문을 써야하는지 검토.
-> 그리고 집합s에 대해서 중복제거처리를 해줘야함.(문제 조건에 간접적으로 나와있었음.)

'''
