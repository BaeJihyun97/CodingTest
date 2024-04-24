# stack

from collections import deque

def solution(number, k):
    answer = ""
    stack = deque()
    length = len(number) - k
    
    for i, n in enumerate(number):
        while k > 0 and len(stack) > 0 and stack[-1] < n:
            stack.pop()
            k -= 1
        stack.append(n)
        
    for i in range(length): answer += str(stack[i])
    
    return answer