from itertools import combinations, product

def count(A, B):
    count = 0
    scoreAl, scoreBl = [], []
    scoreAd, scoreBd = {}, {}
    
    for comb in product(*A):
        scoreAl.append(sum(comb))
    for comb in product(*B):
        scoreBl.append(sum(comb)) 
        
    scoreAl.sort(reverse=True); scoreBl.sort(reverse=True);
    indexA, indexB = 0, 0
    scoreBl_len = len(scoreBl)
    while indexA < len(scoreAl) and indexB < len(scoreBl):
        
        # scoreAl에 같은 숫자 세기
        currAC = 1
        currAV = scoreAl[indexA]
        while indexA < len(scoreAl)-1:
            if scoreAl[indexA+1] == currAV:
                currAC += 1
                indexA += 1
            else: break
        
        while indexB < len(scoreBl):
            if currAV > scoreBl[indexB]: 
                break
            else:
                indexB += 1
                
        count += currAC * (scoreBl_len - indexB)
        indexA += 1
            
    return count

def solution(dice):
    
    n_dice = len(dice)
    dice_index = list(range(n_dice))
    
    
    combs = list(combinations(dice_index, n_dice // 2))
    stats = {key:0 for key in combs}
    for combA in combs:
        combB = tuple([a for a in dice_index if a not in combA])
        stats[combA] = count([dice[i] for i in combA], [dice[i] for i in combB])

    answer = max(stats, key=lambda x: stats[x])
    answer = [i+1 for i in answer]
    return sorted(answer)