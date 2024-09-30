# 구현 문제
from itertools import zip_longest

# 부호 반환
def get_sign(x):
    return -1 if x < 0 else 1

# [a1, a2] 포인트로 이루어진 리스트에서
# 2개 이상 겹친 포인트 개수 반환
def check(points):
    lattice = dict()
    crash = 0
    for pL in points:
        p = tuple(pL)
        if p in lattice:
            if lattice[p] == False: # 2회 이상 충돌 한번만 계산
                lattice[p] = True
                crash += 1
        else:
            lattice[p] = False 
    return crash
                

def solution(points, routes):
    answer = 0
    cache = {} # (s, e) : [[p1, p2] ,...] s -> e 로 가는 s를 제외한 1 step 마다 가야할 포인트 리스트 경로 
    paths = [] # 로봇들이 1 step 마다 가야할 경로들
    
    # 최단 거리 경로 만들기
    for route in routes:
        length = len(route) - 1
        path = [points[route[0]-1]] # 시작점 넣기
        for i in range(length):
            s, e = route[i], route[i+1]
            if (s, e) in cache: # 이전 계산 결과 있음 넣고
                path += cache[(s, e)]
            else:               # 없으면 계산해서 넣기
                [sr, sc], [er, ec] = points[s-1], points[e-1]
                spath = []
                while sr != er: # r 먼저
                    sr -= get_sign(sr - er)
                    spath.append([sr, sc])
                while sc != ec: # c 계산
                    sc -= get_sign(sc - ec)
                    spath.append([sr, sc])
                path += spath
                cache[(s, e)] = spath
        paths.append(path)
        
    paths_T = zip_longest(*paths, fillvalue=None) # 긴 것에 맞춰 zip
    paths_T = [list(filter(lambda p: p!=None, path)) for path in paths_T] # None 값 필터
    for points in paths_T:
        answer += check(points)
                    
    return answer