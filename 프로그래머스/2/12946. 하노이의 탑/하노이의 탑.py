def hanoi(target, curr, other, depth):
    if depth <= 1:
        return [[curr, target]]
    
    answer = hanoi(other, curr, target, depth-1)
    answer += [[curr, target]]
    answer += hanoi(target, other, curr, depth-1)
    return answer

def solution(n):
    return hanoi(3, 1, 2, n)