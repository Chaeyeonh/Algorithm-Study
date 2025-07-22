def solution(brown, yellow):
    answer = []
    total = brown + yellow
    for row in range (3, total+1):
        if total % row == 0:
            col = total // row
            if brown == 2 * (row + col - 2):
                answer.append(row)
                answer.append(col)
                break

    answer.sort(reverse = True)
    return answer