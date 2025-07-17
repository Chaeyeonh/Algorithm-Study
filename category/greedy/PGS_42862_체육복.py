def solution(n, lost, reserve):
    lost_set    = set(lost)
    reserve_set = set(reserve)

    # 1) 자기 빌려주기
    common = lost_set & reserve_set
    lost_set  -= common
    reserve_set -= common

    # answer = 잃지 않은 학생 수 + 자기 자신 빌려준 수
    answer = n - len(lost_set) 

    # 2) 인접 번호 빌려주기: 그냥 얘보다 1큰/작은 애가 있는지만 검사하면됨. O(N)
    for r in reserve_set:
        if r-1 in lost_set:
            lost_set.remove(r-1)
            answer += 1
        elif r+1 in lost_set:
            lost_set.remove(r+1)
            answer += 1

    return answer
