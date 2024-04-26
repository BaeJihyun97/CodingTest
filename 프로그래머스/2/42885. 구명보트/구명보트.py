# 최대 2명! 

def solution(people, limit):
    answer = 0
    
    people.sort(reverse=True)
    s, e = 0, len(people)-1
    count = 0
    
    while s < e:
        w = people[s]
        s += 1
        answer += 1
        count += 1
        
        if w + people[e] <= limit:
            e -= 1
            count += 1
            
    if count < len(people):
        answer += 1
        
    
    
    return answer