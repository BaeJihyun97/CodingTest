from collections import deque

def bfs(numbers, depth, target, value):
    if depth == len(numbers):
        if value == target: 
            return 1
        else: return 0
    
    count = 0
    for coeff in [1, -1]:
        count += bfs(numbers, depth+1, target, value+(numbers[depth]*coeff))

    return count
    


def solution(numbers, target):
    answer = bfs(numbers, 0, target, 0)
    return answer