#분기 한정법: 9가 나온다면 그 뒤의 for문은 더 이상 돌 필요 없으므로 break
def solution(number, k):
    answer = ''
    max_index = -1
    cnt = len(number)-k
    while cnt > 0:
        max = -1
        for i in range (max_index+1,len(number) - cnt + 1):
            if max < int(number[i]):
                max = int(number[i])
                max_index = i
                if max == 9:
                    break
                    
        cnt -= 1
        answer += number[max_index]

    return answer


#stack 풀이

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
def solution(number, k):
    stack = [number[0]]
    for num in number[1:]:
        while len(stack) > 0 and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
        stack.append(num)
    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)