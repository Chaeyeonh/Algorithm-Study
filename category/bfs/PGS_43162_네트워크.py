#동일 문제 BFS 접근법
from collections import deque

def solution(n,computers):
    answer = 0
    visited = [False] * n

    def bfs(start):
        q = deque([start])
        visited[start] = True
        while q:
            v = q.popleft()
            if visited[v] == True:
                continue
            visited[v] = True
            for u in range(n):
                if computers[v][u] == 1 and not visited[v]:
                    visited[u] = True
                    q.push(u)


    for i in range(n):
        if not visited[i]:
            bfs(i)
            answer += 1

    return answer