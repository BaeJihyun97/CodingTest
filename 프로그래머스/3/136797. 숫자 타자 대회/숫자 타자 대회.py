# dfs는 recursionlimit에 걸림. 길이가 100000임
# greedy?

import math

weight_matrix = [[1, 7, 6, 7, 5, 4, 5, 3, 2, 3], 
[7, 1, 2, 4, 2, 3, 5, 4, 5, 6], 
[6, 2, 1, 2, 3, 2, 3, 5, 4, 5], 
[7, 4, 2, 1, 5, 3, 2, 6, 5, 4], 
[5, 2, 3, 5, 1, 2, 4, 2, 3, 5], 
[4, 3, 2, 3, 2, 1, 2, 3, 2, 3], 
[5, 5, 3, 2, 4, 2, 1, 5, 3, 2], 
[3, 4, 5, 6, 2, 3, 5, 1, 2, 4], 
[2, 5, 4, 5, 3, 2, 3, 2, 1, 2], 
[3, 6, 5, 4, 5, 3, 2, 4, 2, 1]]
   

def solution(numbers):
    
    numbers = [int(n) for n in numbers]
    weights = [0 for _ in range(10)]
    
    # 0 단계
    if numbers[0] == 6:  weights[4] += 1
    elif numbers[0] == 4: weights[6] += 1
    else:
        weights[6] += weight_matrix[4][numbers[0]]
        weights[4] += weight_matrix[6][numbers[0]]
    
    # print(weights)
    for i, n in enumerate(numbers[:-1]):
        temps = [0 for _ in range(10)]
        for index, w in enumerate(weights):
            if w != 0:
                # n_i 그대로, n_i 움직이기
                for (move, remain, nxt) in [(index, n, numbers[i+1]), (n, index, numbers[i+1])]:
                    if move != remain:
                        if move != nxt:       # 겹치지 않을 때
                            # print("안겹", "(", move, ":", remain, ":", nxt, ")", temps[n], w + weight_matrix[index][numbers[i+1]])
                            temps[remain] = min(temps[remain], w + weight_matrix[move][nxt]) if temps[remain] != 0 else w + weight_matrix[move][nxt]
                        else:                 # 겹칠 때
                            # print("겹", "(", move, ":", remain, ":", nxt, ")", temps[n], w + 1)
                            temps[remain] = min(temps[remain], w + 1) if temps[remain] != 0 else w + 1
        
        # print(temps)
        weights.clear()
        weights = temps              
    
    return min([w for w in weights if w != 0])



## weight_matrix로 대체
# def count(a, b):
#     if a == b:
#         return 1
#     dic = {1:(0, 0), 2:(0, 1), 3:(0, 2), 4:(1, 0), 5:(1, 1), 6:(1, 2), 7:(2, 0), 8:(2, 1), 9:(2, 2), 0:(3, 1)}
    
#     start, end = dic[a], dic[b]
#     x_distance, y_distance = abs(start[0]-end[0]), abs(start[1]-end[1])
#     weight = 0
    
#     while x_distance > 0 and y_distance > 0:
#         weight += 3
#         x_distance -= 1; y_distance -= 1
        
#     if x_distance > 0:
#         weight += x_distance*2
#     elif y_distance > 0:
#         weight += y_distance*2

#     return weight