#백준 24480; bfs 문제.

import sys
sys.setrecursionlimit(10**9)

def dfs(start):
    global count
    visited[start] = count
    graph[start].sort(reverse = True)
    
    for i in graph[start]:
        if visited[i] == 0:
            count += 1
            dfs(i)

v, e, s = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(v+1)]
visited = [0]*(v+1)
count = 1

for _ in range(e): # 간선입력
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x) ## 그래프 구현
    
dfs(s)

for x in range(1,v+1):
    print(visited[x])
