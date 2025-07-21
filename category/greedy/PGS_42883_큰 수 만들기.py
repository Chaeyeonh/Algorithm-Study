
def solution(number, k):
    answer = ''
    max_index = -1
    k = len(number)-k
    while k > 0:
        max = -1
        for i in range (max_index+1,len(number) - k + 1):
            if max < int(number[i]):
                max = int(number[i])
                max_index = i
                if max == '9':
                 break
        k -= 1
        answer += number[max_index]

        print('max_index:',max_index)

        print('k',k)
        print('answer:',answer)

    return answer

print(solution('1231234',3))
#테스트 케이스 10번 시간 초과 오류. 시간복잡도 O(N^2)라서...