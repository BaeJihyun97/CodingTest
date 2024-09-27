def calculate(puzzles, level):
    time = 0
    
    for p in puzzles:
        diff, time_cur, time_prev = p
        if diff <= level:
            time += time_cur
        else:
            time += (diff - level) * (time_cur + time_prev) + time_cur
        
    return time

def solution(diffs, times, limit):
    answer = 0
    time_prevs = [0] + times[:-1]
    
    puzzles = [[d, t, p] for d, t, p in zip(diffs, times, time_prevs)]
    puzzles.sort(key = lambda x:x[0])
    
    minV, maxV = 1, puzzles[-1][0]
    prev, poss = 0, False
    
    while minV <= maxV:
        answer = (minV + maxV) // 2
        time = calculate(puzzles, answer)
        # print(f"min:{minV}, max:{maxV}, curr:{answer}, time:{time}")
        if time > limit:
            minV, prev, poss = answer+1, answer, False
        elif time < limit:
            if minV == maxV:
                break
            else:
                maxV, prev, poss = answer, answer, True
        else:
            break

    return answer