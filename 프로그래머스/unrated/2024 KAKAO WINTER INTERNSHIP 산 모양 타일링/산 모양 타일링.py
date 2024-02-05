from collections import deque
from itertools import combinations

def solution(n, tops):
    answer = 0
    # init
    A = [4] if tops[0] == 1 else [3] # answer
    B = [3] if tops[0] == 1 else [2] 
    
    # A'(i) = [2*A'(i-1) + B'(i-1), A'(i-1) if top[i]==1 else 0] -> 속도를 위해 A(i) = sum(A'(i))
    #         /\                    /\                 /\                  /\
    #  ~~~~~~/__\     top[i]==0    /__\ __            /__\ __             /__\ __
    #       /\  /\      =>>       /\  /\  /\         /\  /\   \          /\  /   /\
    #  ~~~~/__\/__\           ~~~/__\/__\/__\    ~~~/__\/__\ __\     ~~~/__\/__ /__\
    #      (A(i-1))                 A(i-1)             A(i-1)             B(i-1)
    #                            
    #                               /\  /\
    #                 top[i]==1    /__\/  \
    #                   =>>       /\  /\  /\
    #                         ~~~/__\/__\/__\
    #                               A(i-1)
    # B'(i) = [A'(i-1) + B'(i-1), A'(i-1) if top[i]==1 else 0] -> 속도를 위해 B(i) = sum(B'(i))
    #         /\                    /\                 /\               
    #  ~~~~~~/__\     top[i]==0    /__\ __            /__\ __            
    #       /\  /       =>>       /\  /\  /          /\  /   /         
    #  ~~~~/__\/              ~~~/__\/__\/       ~~~/__\/__ /         
    #      (B(i-1))                 A(i-1)             B(i-1)        
    #                            
    #                               /\  /\
    #                 top[i]==1    /__\/  \
    #                   =>>       /\  /\  / 
    #                         ~~~/__\/__\/   
    #                               A(i-1)
    for i in range(1, n):
        tempA = A[i-1] * 2 + B[i-1]
        tempB = A[i-1] + B[i-1]
        
        if tops[i] == 1:
            tempA += A[i-1]
            tempB += A[i-1]
            
        A.append(tempA % 10007)
        B.append(tempB % 10007)
        
    answer = A[-1]     
    
    return answer

