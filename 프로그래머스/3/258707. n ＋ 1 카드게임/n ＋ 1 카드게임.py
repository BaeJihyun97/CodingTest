
#========================================================================
# making Pair (i, n n- i +1)
# return: pairList: list
#         element: {"value":(i, n n- i +1), "coin": coin, "round", round}
#                   coin: 필요한 코인 수 [0, 1, 2] 중 하나
#                   round: 해당 페어를 낼 수 있는 최소 라운드 수 1~n/3 범위 안.
#========================================================================
def makePair(cards):
    pairList = []
    n = len(cards)
    indexList = [0] * (n+1)
    
    for index, card in enumerate(cards):
        indexList[card] = index + 1
        
    for i in range(1, n // 2 + 1):
        roundl, roundr = max(((indexList[i] - n // 3) + 1)// 2, 1), max(((indexList[n-i+1] - n // 3) + 1)// 2, 1)
        coin = 0
        if indexList[i] > n // 3: coin +=1
        if indexList[n-i+1] > n // 3: coin +=1
        pairList.append({"value":(i, n-i+1), "coin":coin, "round": max(roundl, roundr)})
        
    return pairList

def splitPair(pairList):
    que0, que1, que2 = [], [], [] # 범위가 작고, 한번에 정렬해도 가능하니, python 내장 함수 sort 사용
    for pair in pairList:
        if pair["coin"] == 0:
            que0.append(pair["round"])
        elif pair["coin"] == 1:
            que1.append(pair["round"])
        else:
            que2.append(pair["round"])
    
    que0.sort(); que1.sort(); que2.sort()
    return que0, que1, que2
    

def solution(coin, cards):
    answer = 0
    
    # 전처리
    pairList = makePair(cards)
    que0, que1, que2 = splitPair(pairList)
    
    maxround = 1 + len(que0)
    # print("0", maxround, coin)
    while True:
        flag = False
        # coin1 que에서 가져올 수 있는 만큼 가져오기
        while coin > 0:
            if  len(que1) > 0 and que1[0] <= maxround:
                maxround += 1
                coin -= 1
                flag = True
                que1.pop(0)
                # print("1", maxround, coin)
            else:
                break
        
        # coin2는 하나만 가져오고 coin1 다시 보기
        if coin > 1:
            if  len(que2) > 0 and que2[0] <= maxround:
                maxround += 1
                coin -= 2
                flag = True
                que2.pop(0)
                # print("2", maxround, coin)

        
        # coin1 que, coin2 que 에서 한번도 가져오지 못하면 게임 끝
        if flag == False:
            break
    
    answer = min(maxround, len(cards)//3 +1)
    return answer



