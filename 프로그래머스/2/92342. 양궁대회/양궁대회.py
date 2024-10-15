# 알고리즘: DFS
# 자료구조: list
# 주의: 경우의 수가 2**20 밑이어야 가능
#       경우의 수를 줄이기 위해, 동일한 경우는 다시 처리하지 않게
#       동일하다고 여겨지는 경우의 수는 계산하지 한번만 처리할 수 있도록

def calculate(apeach_info, lion_info):
    score = 0
    for index, (a, l) in enumerate(zip(apeach_info, lion_info)):
        if a != 0 or l != 0:
            if a >= l:
                score -= 10 - index
            else:
                score += 10 - index
    return score

def isSmaller(a, b):
    if len(a) != len(b):
        return False
    
    for a_, b_ in zip(a[::-1], b[::-1]):
        if a_ < b_:
            return True
        elif a_ > b_:
            return False
    return False
            

def DFS(n, apeach_info, lion_info, depth, remain):
    if depth == 11:
        return calculate(apeach_info, lion_info), lion_info[:]
    
    score = -1
    answer = [-1]
    
    for ith_score in [0, apeach_info[depth] + 1]:
        if ith_score <= remain:
            lion_info[depth] = ith_score
            score_, lion_info_ = DFS(n, apeach_info, lion_info, depth+1, remain-ith_score)
            
            if score_ > score and score_ > 0:
                score = score_
                answer = lion_info_
            elif score_ == score and isSmaller(answer, lion_info_):
                answer = lion_info_
                
    return score, answer

def solution(n, info):
    score, answer = DFS(n, info, [0]*11, 0, n)
    sum_lion = sum(answer)
    if score > 0 and sum_lion < n:
        answer[-1] += n - sum_lion

    return answer