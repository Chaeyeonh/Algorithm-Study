def solution(arr):
    answer = []
    for i in arr:
        if len(answer) == 0 or answer[-1] != i:
            answer.append(i)
    return answer

print(solution("133303")) # [1,3,0,3]