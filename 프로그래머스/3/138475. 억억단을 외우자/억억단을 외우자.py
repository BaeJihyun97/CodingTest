def solution(e, starts):
    answers = []
    counts = [0 for _ in range(e+1)]
    
    for i in range(1, e+1):
        k1 = i*i
        if k1 <= e: counts[k1] += 1
        
        for j in range(i+1, e+1):
            k2 = i*j
            if k2 > e: break
            counts[k2] += 2
    
    maxs = [0 for _ in range(e+1)]
    maxV, maxI = 0, 0
    for index in range(e, 0, -1):
        if counts[index] >= maxV:
            maxV = counts[index]
            maxI = index
        maxs[index] = maxI
    
    for s in starts:
        answers.append(maxs[s])
        
    return answers