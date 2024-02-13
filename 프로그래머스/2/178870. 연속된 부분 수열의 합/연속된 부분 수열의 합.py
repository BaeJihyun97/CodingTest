def solution(sequence, k):
    
    end = len(sequence)-1
    
    while sequence[end] > k:
        end -= 1
        
        
    start = end
    sumv = sequence[end]
    while start <= end:
        if sumv == k: 
            break
        elif sumv < k:
            start -= 1
            sumv += sequence[start]
        else: # sumv > k
            sumv -= sequence[end]
            end -= 1

    
    while start > 0 and sequence[start-1] == sequence[end]:
        start -= 1
        end -= 1
    
    answer = [start, end]
    return answer