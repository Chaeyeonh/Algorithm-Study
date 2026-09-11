from collections import deque

def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])

    q = deque([(0,0)])
    while q:
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]
        x,y = q.popleft()

        for i in range(4):

            nx = x + dx[i]
            ny = y + dy[i]
            if nx< 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if maps[nx][ny] == 0:
                continue
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                q.append((nx,ny))
                
    answer = maps[n-1][m-1] 
    return answer if answer>1 else -1