# 알고리즘: dp
# 자료구조: list + set
# 주의: dp가 꼭 배열 형태에 dp[i] = dp[curr] + weight 로 업데이트 할 필요는 없음
#       이전 단계의 데이터를 저장하고, 다음 단계에서 쓴다!
#       dp[k] = set(N을 k 번 써서 만들 수 있는 수) 로 하고 k + 1 단계에서 dp[1] ~ dp[k-1] 수들 쓰기
#       겹치는 건 틈틈히 set 로 써서 중복 줄이기!

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