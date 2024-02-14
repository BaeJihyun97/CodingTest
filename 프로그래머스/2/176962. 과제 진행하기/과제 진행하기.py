def solution(plans):
    answer = []
    onprogress = []
    # 편의를 위해 시간을 분으로 바꾸기. ex)11:40 => 11*60 + 40 = 700
    for plan in plans:
        time = plan[1]
        hour, minute = map(int, time.split(":"))
        plan[1] = hour*60 + minute
        plan[2] = int(plan[2])
        
    # 시간 순으로 정렬
    plans.sort(key = lambda x: x[1])
    
    # 각 과제 시작 시간마다 plans 상태 업데이트
    prev = plans[0]
    for plan in plans[1:]:
        term = plan[1] - prev[1]
        if prev[2] <= term: 
            answer.append(prev[0])
            remain = term - prev[2]
            while remain > 0 and len(onprogress) > 0:
                p = onprogress[-1]
                if p[2] <= remain:
                    answer.append(p[0])
                    onprogress.pop(-1)
                    remain -= p[2]
                else:
                    p[2] -= remain
                    remain = 0
        else:
            prev[2] -= term
            onprogress.append(prev)
        prev = plan
    
    onprogress.append(plans[-1])
    onprogress.reverse()
    answer = answer + [p[0] for p in onprogress]
    return answer