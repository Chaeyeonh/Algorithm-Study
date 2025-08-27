function solution(maps) {
    var answer = 0;
    const n = maps.length;
    const m = maps[0].length;
    const dx = [-1,1,0,0];
    const dy = [0,0,-1,1];
    
    const queue = [[0,0]];
    
    while (queue.length){
        let [x,y] = queue.shift();
        for (let i = 0; i<4; i++){
            let nx = x + dx[i];
            let ny = y + dy[i];
            if (nx < 0 || ny < 0 || nx >= n || ny >= m || maps[nx][ny]              === 0){
                continue;
            }
            if (maps[nx][ny] === 1){
                maps[nx][ny] = maps[x][y] + 1;
                queue.push([nx,ny]);
            }
        }
        
    }
    answer = maps[n-1][m-1];
    return answer > 1 ? answer : -1;
}