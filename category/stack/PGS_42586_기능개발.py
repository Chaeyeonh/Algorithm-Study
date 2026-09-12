def solution(progresses, speeds):
    answer = []
    days = []
    
    for p, s in zip(progresses, speeds):
        remaining_work = 100 - p
        day = (remaining_work + s - 1) // s  # Calculate the days needed to complete the work
        days.append(day)
    
    current_max_day = days[0]
    count = 1
    
    for i in range(1, len(days)):
        if days[i] <= current_max_day:
            count += 1
        else:
            answer.append(count)
            count = 1
            current_max_day = days[i]
    
    answer.append(count)  # Append the last count
    
    return answer


def solution(progresses,speeds):
    answer = []
    time = 0
    count = 0 
    while len(progresses) > 0:
        
        if (progresses[0] + time * speeds[0] >= 100):
            progresses.pop(0)
            speeds.pop(0)
            count += 1
            

        else:
            if count > 0:
                count = 0
                answer.append(count)
            time += 1
    answer.append(count)
    return answer