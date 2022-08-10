# 백준 2644번; 촌수계산 ->dfs로 풀이함.
import sys
sys.setrecursionlimit(10**9)

n = int(sys.stdin.readline()) # node
a,b = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline()) # edges
graph = [[] for _ in range(n+1)]
visited = [0]*(n+1) # a를 기준으로 a와 b의 촌수거리를 저장. a자신은 0으로 저장. 즉, visited[a]=0 이다.


def dfs(x,c):
    visited[x] = c
    for i in graph[x]:
        if visited[i] == 0:
            dfs(i,c+1) # 촌수거리에 +1 처리.
    


for i in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)



dfs(a,0) # 시작 정점 a와 촌수거리 0을 인자로 전달.

if visited[b] != 0:
    print(visited[b])
else:
    print(-1)
