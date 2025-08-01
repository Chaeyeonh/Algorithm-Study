function solution(numbers, target) {
    var answer = 0;
    
    function dfs(idx, current_sum){
        if (idx === numbers.length){
            if (current_sum === target){
                answer += 1;
            }
            return;
        }
        dfs(idx + 1, current_sum + numbers[idx]);
        dfs(idx + 1, current_sum - numbers[idx]);
    }
    dfs(0,0)
    return answer;
}