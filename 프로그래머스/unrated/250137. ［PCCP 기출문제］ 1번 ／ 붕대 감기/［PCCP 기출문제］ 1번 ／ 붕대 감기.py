def solution(bandage, health, attacks):
    answer = health
    last_time = attacks[-1][0]
    comb = 0
    
    for i in range(last_time + 1):
        if attacks[0][0] == i:
            attack = attacks.pop(0)[1]
        else:
            attack = -1
        
        # no attack
        if attack == -1:
            comb += 1
            answer += bandage[1]
            if comb == bandage[0]:
                answer += bandage[2]
                comb = 0
            if answer > health:
                answer = health
        # attack    
        else:
            answer -= attack
            comb = 0

            
        # 공격 후 체력이 0 이하면 죽음.
        if answer <= 0:
            answer = -1
            break

    
    return answer