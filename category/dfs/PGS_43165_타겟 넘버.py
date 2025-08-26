#1
def solution(numbers, target):
    answer = 0
    def dfs(idx, current_sum):
        nonlocal answer #내포 함수가 바깥 함수의 변수에 접근할 수 있도록
        if idx == len(numbers):
            if current_sum == target:
                answer += 1
            return
        
        dfs(idx+1, current_sum + numbers[idx])
        dfs(idx+1, current_sum - numbers[idx])
    
    dfs(0,0) 
    return answer

#2
def solution(numbers, target):
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])
    

#3
from itertools import product
def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target)