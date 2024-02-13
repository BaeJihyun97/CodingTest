def solution(targets):
    answer = 0
    targets.sort(key = lambda x: x[0])
    
    # print(targets)
    
    target = targets.pop(0)
    targetmax = target[1]
    answer += 1
    for curr in targets:
        # print("curr:", curr)
        if curr[0] < target[1] and curr[0] < targetmax:
            targetmax = min(curr[1], targetmax)
        else:
            target = curr
            targetmax = curr[1]
            answer += 1
            # print(target)
    return answer