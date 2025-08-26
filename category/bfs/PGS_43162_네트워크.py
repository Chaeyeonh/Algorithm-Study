from collections import deque

def solution(n, computers):
    answer = 0
    visited = [False] * n

    def bfs(start):
        q = deque([start])
        visited[start] = True                 # 큐에 넣는 순간 방문 표시
        while q:
            v = q.popleft()
            for u in range(n):
                if computers[v][u] == 1 and not visited[u]:
                    visited[u] = True         # 중복 삽입 방지
                    q.append(u)

    for i in range(n):
        if not visited[i]:                    # 새로운 네트워크 시작점
            bfs(i)
            answer += 1

    return answer
