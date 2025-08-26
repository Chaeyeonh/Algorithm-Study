function solution(n,computers){
    let answer = 0
    const visited = new Array(n).fill(false);

    const dfs = (start) => {
        const stack = [start];
        while(stack.length){
            const v = stack.pop();
            for (let u = 0; u <n; u++){
                if (computers[v][u] === 1 && !visited[u]) stack.push(u);
            }
        }
    }

    for(let i = 0; i<n; i++){
        if(!visited[i]){
            dfs(i);
            answer++;
        }
    }
    return answer;
}