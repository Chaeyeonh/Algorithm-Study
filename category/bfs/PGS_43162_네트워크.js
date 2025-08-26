//네트워크 bfs풀이
function solution(n, computers){
    const visited = Array(n).fill(false);
    let answer = 0;

    const bfs = (start) => {
        const queue = [start];
        visited[start] = true;
        while(queue.length > 0){
            const v = queue.shift();
            
            for (let u = 0; u < n; u++){
                if (computers[u][v] === 1 && !visited[u]){
                    visited[u] = true;
                    queue.push(u);
                }
            }
        }
    }

    for (let i = 0; i < n; i++){
        if (visited[i] === false){
            bfs(i);
            answer ++;
        }
    }

    return answer;

}