from collections import deque
import heapq

def operate(dpi, dpj, temp, tot_set):
    # +-*/
    for i in dpi:
        for j in dpj:
            if j != 0:
                for num in [i+j, i-j, i*j, i//j]:
                    if num not in tot_set:
                        temp.add(num)
                        tot_set.add(num)
    return
    
    

def solution(N, number):
    answer = -1
    MAXV =  2*number + 1
    rpt_N = N
    dp = [set()]
    tot_set = set([])

    # 1 개 사용
    if number == rpt_N:
        return 1
    dp.append(set([rpt_N]))
    tot_set.add(rpt_N)
    
    
    # 2 ~ 8 개 사용
    for k in range(2, 9):
        rpt_N = rpt_N*10 + N
        temp = set()
        temp.add(rpt_N)
        
        for i in range(1, k):
            j = k-i
            operate(dp[i], dp[j], temp, tot_set)
            
        if number in temp:
            answer = k
            break
            
        dp.append(temp)
        
    
    return answer