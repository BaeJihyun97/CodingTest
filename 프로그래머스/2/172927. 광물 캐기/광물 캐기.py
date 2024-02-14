def solution(picks, minerals):
    answer = 0
    mineral5 = []
    possible = sum(picks)
    # 5개 연속, 피로도가 5의 배수이니
    # dia, iron, stone 순으로 정렬한 순서대로 dia, iron, stone 곡괭이 사용
    # 주의!! minerals의 개수는 5의 배수가 아님.
    for i in range(0, len(minerals), 5):
        mineral5.append([minerals[i:i+5].count("diamond"), minerals[i:i+5].count("iron"), minerals[i:i+5].count("stone")])
    
    
    mineral5 = mineral5[:min(possible, len(mineral5))]
    mineral5.sort(reverse=True, key = lambda x: (x[0], x[1]))
    
    
    for [dia, iron, stone] in mineral5:
        if picks[0] > 0:
            picks[0] -= 1
            answer += dia + iron + stone
        elif picks[1] > 0:
            picks[1] -= 1
            answer += dia * 5 + iron + stone
        else:
            picks[2] -= 1
            answer += dia * 25 + iron * 5 + stone
    
    return answer