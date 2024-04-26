# 요격 시스템과 같은 문제

def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[0])
    count, maxCount = 0, len(routes)
    
    while count < maxCount:
        curr = routes[count]
        maxStart = curr[1]
        answer += 1
        count += 1
        
        while count < maxCount and routes[count][0] <= maxStart:
            maxStart = min(maxStart, routes[count][1]) # curr 하고만 비교하는 것이 아니라 이전 것들과도 비교!!!!
            count += 1
            
    return answer