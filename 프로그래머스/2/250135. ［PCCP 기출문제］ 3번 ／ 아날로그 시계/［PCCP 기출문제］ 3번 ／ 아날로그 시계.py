HOUR_S = 1/120
MINUTE_S = 1/10
SECOND_S = 6
HOUR_M = 1/2
MINUTE_M = 6
HOUR_H = 30

# 0:0:0 과 12:0:0 시 포함 여부
def find00(h1, m1, s1, h2, m2, s2):
    count = 0
    if h1 == 0 and m1 == 0 and s1 == 0:
        count += 1
    if h1 <= 12 and h2 >= 12:
        count += 1
    
    return count

# 12:0:0 시 포함 여부 
def find12(h1, m1, s1, h2, m2, s2):
    if check(h1, m1, s1, 12, 0, 1) and check(12, 0, 0, h2, m2, s2):
        return True
    else:
        return False

# h1시 m1분 s1초 < h2시 m2분 s2초 확인
def check(h1, m1, s1, h2, m2, s2):
    if h1 < h2:
        return True
    elif h1 == h2 and m1 < m2:
        return True
    elif h1 == h2 and m1== m2 and s1 < s2:
        return True
    else:
        return False
    
def plus_1s(h1, m1, s1):
    s1 += 1
    if s1 >= 60:
        s1 = s1 % 60
        m1 += 1
        if m1 >= 60:
            m1 = m1 % 60
            h1 += 1
    return h1, m1, s1

# 360' 빼기 계산에서 예각 찾기
def minus(a, b):
    answer = abs(a - b)
    return min(answer, 360 - answer)

# 왼쪽(반시계)/ 오른쪽(시계) 확인 b 기준 a가 오른쪽에 있으면 true
def RLcheck(a, b):
    b2 = (b + 180) % 360
    if b < b2:
        if a > b and a < b2:
            return True
        else:
            return False
    else:
        if a > b2 and a < b:
            return False
        else:
            return True
            
   


def solution(h1, m1, s1, h2, m2, s2):
    count = find00(h1, m1, s1, h2, m2, s2)
    answer = 0
    index = 0
    
    if h1 == 0 and m1 == 0 and s1 == 0:
        answer -= 1
    if find12(h1, m1, s1, h2, m2, s2):
        answer -= 1
    
    while(check(h1, m1, s1, h2, m2, s2)):
        secondP_B = (s1 * SECOND_S) % 360
        minuteP_B = ((m1 * MINUTE_M) + (s1 * MINUTE_S)) % 360
        hourP_B = ((h1 * HOUR_H) + (m1 * HOUR_M) + (s1 * HOUR_S)) % 360
        
        
        h1, m1, s1 = plus_1s(h1, m1, s1)
        
        secondP_N = (s1 * SECOND_S) % 360
        minuteP_N = ((m1 * MINUTE_M) + (s1 * MINUTE_S)) % 360
        hourP_N = ((h1 * HOUR_H) + (m1 * HOUR_M) + (s1 * HOUR_S)) % 360
        
        if (minus(minuteP_B, secondP_B) < 6 - MINUTE_S) and RLcheck(secondP_B, minuteP_B) ^ RLcheck(secondP_N, minuteP_N):
            answer += 1
        if (minus(hourP_B, secondP_B) < 6 - HOUR_S) and RLcheck(secondP_B, hourP_B) ^ RLcheck(secondP_N, hourP_N):
            answer += 1
        
            
    

    if m2 == 0 and s2 == 0:
        answer += 1   


    
    return answer