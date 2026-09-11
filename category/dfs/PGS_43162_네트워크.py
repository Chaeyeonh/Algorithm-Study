
def solution(n,computers):
    answer = 0
    graph = [[] for _ in range(n)]

    #인접 리스트 생성
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                graph[i].append(j)
    
    def dfs(v, graph, visited):
        visited[v] = True
        for k in graph[v]:
            if not visited[k]:
                dfs(k, graph, visited)


    visited = [False] * n

    for i in range(n):
        if not visited[i]:
            dfs(i,graph,visited)
            answer += 1

    return answer


#스택으로 풀기
def solution(n,computers):
    answer = 0
    visited = [0] * n

    def dfs_stack(start):
        stack = [start]
        while stack:
            v = stack.pop()
            if visited[v]:
                continue
            visited[v] = 1
            for u in range(n):
                if computers[v][u] == 1 and not visited[u]:
                    stack.append(u)

    for i in range(n):
        if not visited[i]:
            dfs_stack(i)
            answer += 1
            
    return answer