
def solution(number, k):
    answer = ''
    max_index = -1
    k = len(number)-k
    while k > 0:
        max = 0
        for i in range (max_index+1,len(number) - k + 1):
            if max < int(number[i]):
                max = int(number[i])
                max_index = i
        k -= 1
        answer += number[max_index]

        print('max_index:',max_index)

        print('k',k)
        print('answer:',answer)

    return answer

print(solution('1231234',3))