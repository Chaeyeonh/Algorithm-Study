from itertools import permutations

def solution(k, dungeons):
    max_clear = 0

    for perm in permutations(dungeons):
        cur_k = k
        cnt = 0
        for need, use in perm:
            if cur_k >= need:
                cur_k -= use
                cnt += 1
            else:
                break
        max_clear = max(max_clear, cnt)

    return max_clear
