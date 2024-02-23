import operator

# greedy?
def countWaiting(counselor, reqs):
    possible = {key:[0 for _ in range(value)] for key, value in counselor.items()}
    waiting = {key:0 for key, _ in counselor.items()}
    for req in reqs:
        [start, period, category] = req
        earliest = min(possible[category])
        earliest_index = possible[category].index(earliest)
        if earliest <= start:
            possible[category][earliest_index] = start + period
        else:
            possible[category][earliest_index] += period
            waiting[category] += earliest - start
    
    return waiting
            
        

def findCounselor(counselor, reqs, k):
    waitings = []
    for category in range(1, k+1):
        counselor_can = {key:value for key, value in counselor.items()}
        counselor_can[category] += 1
        waiting = countWaiting(counselor_can, reqs)
        waitings.append(sum([v for k, v in waiting.items()]))
    
    return waitings.index(min(waitings)) + 1

def solution(k, n, reqs):
    answer = 0
    counselor = {key:1 for key in range(1, k+1)}
    
    for _ in range(n-k):
        added_counselor = findCounselor(counselor, reqs, k)
        counselor[added_counselor] += 1
        
    waiting = countWaiting(counselor, reqs)
    for key, value in  waiting.items():
        answer += value
    return answer