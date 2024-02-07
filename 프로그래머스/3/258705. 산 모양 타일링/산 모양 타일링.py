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


#     TIME OUT
#     bottom = [0]*(n+1)
#     bottom[0:3] = [1, 3, 8]
#     bottom_sum = [0, 3, 11]
#     que = deque()
    
#     for i in range(2, n):
#         bottom[i+1] = (bottom[i]*2 + bottom[i-2] + 2*bottom_sum[i-2] +4) % 10007
#         bottom_sum.append((bottom_sum[-1]+bottom[i+1] % 10007))
        
    
#     if 1 not in tops:
#         answer = bottom[n] 
#     else:

#         top_index = [i+1 for i, v in enumerate(tops) if v == 1]
#         top_count = sum(tops)

#         answer = bottom[n]
                
#         for i in range(1, top_count+1):
#             for combs in combinations(top_index, i):
#                 temp = [0] + list(combs) + [n+1]
#                 comb_distance = [temp[i] - temp[i-1] - 1 for i in range(1, i+2)]
#                 addition = 1
#                 for t in comb_distance:
#                     addition = (addition*bottom[t]) % 10007
#                 answer += addition
#                 answer %= 10007

