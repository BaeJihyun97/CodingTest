from copy import deepcopy
from collections import deque
from sys import maxsize

ANSMAX = maxsize


# 모두 12시 방향인지 확인하는 함수
def check(clockHands):    
    for clockHand in clockHands:
        for hand in clockHand:
            if hand != 0:
                return False
    return True

# 마지막 행이 12시 방향인지 확인하는 함수
def check2(clockHands):    
    for hand in clockHands[-1]:
        if hand != 0:
            return False
    return True


# 방향을 바꾸는 함수
def change(clockHands, i, j, n):
    row, col = len(clockHands), len(clockHands[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (0, 0)]
    
    for (r, c) in directions:
        x, y = r+i, c+j
        if x >= 0 and x < row and y >= 0 and y < col:
            clockHands[x][y] = (clockHands[x][y] + n) % 4
    return


# 첫번째 행을 기준으로 12시 만들기
def calculate(clockHands):
    N = len(clockHands)
    tempHands = deepcopy(clockHands)
    answer = 0
    
    for i in range(N-1):
        for j in range(N):
            n = (4-tempHands[i][j]) % 4
            change(tempHands, i+1, j, n)
            answer += n
            
    if not check2(tempHands):
        answer = ANSMAX

    return answer


# 첫번째 행으로 전체 탐색.
# [0, 0, ..., 0] ~ [3, 3, ..., 3]
def dfs(clockHands, firstRow, depth, n):
    if depth == n:
        return calculate(clockHands) + sum(firstRow) # !실수!: 첫번째 행도 돌렸다는 것을 잊지 말자
    
    answer = ANSMAX
    for c in range(4):
        firstRow_ = firstRow + [c]
        change(clockHands, 0, len(firstRow_)-1, c)
        answer = min(dfs(clockHands, firstRow_, depth+1, n), answer)
        change(clockHands, 0, len(firstRow_)-1, -c)
        
    return answer        


def solution(clockHands):
    answer = 0
    N = len(clockHands)

    if check(clockHands):
        return answer
    
    # 모든 위치에 선택 대한 전체탐색은 시간 초과(특징1과 특징2를 쓰더라도)
    # 특징1: 돌리는 순서는 결과에 영향을 주지 않는다
    # 특징2: '자신이 돌린 횟수'는 4 이하
    # 특징3: 한 위치가 돌려진 횟수는 '자신이 돌린 횟수' + '인접 위치가 돌린 횟수' ( % 4 ) 
    # 전체탐색 범위를 줄여야함.
    # 테두리에 있는 하나의 행(열)이 각각 a_0i번 회전했다고 하면
    # 모두 12시 방향을 갖게하기 위해서는 그 다음 행의 회전 횟수 a_1i번의 회전 횟수가 정해짐. <- 모든 위치 전체 탐색은 이 특징 이용 안한거
    # 만일 이 회전 수가 정답이라면 마지막 행이 모두 12시 방향
    # 4^(N) 번 최대 4^8 번 안에 가능

    return dfs(clockHands, [], 0, N)
