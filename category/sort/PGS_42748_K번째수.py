def solution(array, commands):
    answer = []
    for i in range (len(commands)):
        sliced_array = sorted(array[int(commands[i][0])-1:commands[i][1]])
        answer.append(sliced_array[int(commands[i][2])-1])
    return answer


#다른 사람의 풀이

def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))