from itertools import combinations

def solution(friends, gifts):
    answer = [0] * len(friends)
    
    ## 전처리
    friends_dict = {key:i for i, key in enumerate(friends)}
    gift_matrix = [[0]* len(friends) for _ in range(len(friends))]
    gift_point = [0] * len(friends)
    
    # 선물 matrix 만들기
    for gift in gifts:
        [giver, reciever] = gift.split(" ")
        giver, reciever = friends_dict[giver], friends_dict[reciever]
        gift_matrix[giver][reciever] += 1
        gift_point[reciever] += 1
    
    # 선물 지수 만들기
    for i in range(len(gift_point)):
        gift_point[i] = sum(gift_matrix[i]) - gift_point[i]
        
    ## 다음달 계산하기
    for (A, B) in combinations(list(range(len(friends))), 2):
        # 주고받은 기록이 하나도 없거나 주고받은 수가 같다면
        if (gift_matrix[A][B] == 0 and gift_matrix[B][A] == 0) or \
            gift_matrix[A][B] == gift_matrix[B][A]:
            if gift_point[A] > gift_point[B]:
                answer[A] += 1
            elif gift_point[A] < gift_point[B]:
                answer[B] += 1
        
        else:
            if gift_matrix[A][B] > gift_matrix[B][A]:
                answer[A] += 1
            else:
                answer[B] += 1
        
    
    return max(answer)