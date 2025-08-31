def solution(array, commands):
    answer = []
    for i in range (len(commands)):
        sliced_array = sorted(array[int(commands[i][0])-1:commands[i][1]])
        answer.append(sliced_array[int(commands[i][2])-1])
    return answer