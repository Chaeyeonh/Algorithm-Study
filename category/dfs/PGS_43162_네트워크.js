
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
function solution(n,computers){
    let answer = 0
    const visited = new Array(n).fill(false);

    const dfs = (start) => {
        const stack = [start];

        while(stack.length){
            const v = stack.pop();

            if(visited[v] === true){
                continue;
            }
            visited[v] = true;
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
