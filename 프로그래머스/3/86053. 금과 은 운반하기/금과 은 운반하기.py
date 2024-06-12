# 이분 탐색 Parametric Search 유형

# 시간이 주어졌을 때 목표를 완료할 수 있는 지
def check(time, a, b, g, s, w, t):
    # 한 도시에는 하나의 트럭이지만 제한 무게 안에 금과 은 한번에 배달 가능
    # totalW, goldW, silverW 변수 3개 필요
    totalW, goldW, silverW = 0, 0, 0
    
    for gi, si, wi, ti in zip(g, s, w, t):
        # i 번째 도시의 트럭이 time 시간동안 운반할 수 있는 횟수
        count = time // (2*ti)
        count += (time - count*2*ti) // ti

        totalW += min(count * wi, gi + si)
        goldW += min(count * wi, gi)
        silverW += min(count * wi, si)
        
    if totalW >= (a + b) and goldW >= a and silverW >= b:
        return True
    else:
        return False
    

def solution(a, b, g, s, w, t):
    minV, avgV, maxV = 0, 0, 4e14
    
    while minV + 1 < maxV:
        avgV = (minV + maxV) // 2
        if check(avgV, a, b, g, s, w, t):
            maxV = avgV
        else:
            minV = avgV
    

    return maxV