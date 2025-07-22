def solution(brown, yellow):

    total = brown + yellow
    for row in range (3, int(total**1/2) + 1):
        if total % row == 0:
            col = total // row
            if brown == 2 * (row + col - 2):
                break

    return [col,row]