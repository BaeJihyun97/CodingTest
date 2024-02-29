from collections import deque

def nextAction(T, t1, t2, a, b, onboard, currE):
    [index, cost, curT, on] = currE
                
    nextActions = [a, b, 0] if on else [a, 0]
    nextElements = []

    for c in nextActions:
        nextT, on = curT, True
        if c == a:
            if T > t2: nextT -= 1
            else: nextT += 1
        elif c == b:
            pass
        else:
            on = False
            if T > t2: nextT = min(nextT+1, T)
            else: nextT = max(nextT-1, T) 
            
            
        nextElements.append([index+1, cost+c, nextT, on])
    
    return nextElements

def check(nextElements, onboard, t1, t2):
    return_list = []
    temperatures = [-1]*51
    ons = [False]*51
    nextindex = nextElements[0][0]
    person = onboard[nextindex]
    for index, cost, curT, on in nextElements:
        if curT > 40 or curT < -10 or (person  == 1 and (curT > t2 or curT < t1)):
            continue
        if temperatures[curT] == -1 or temperatures[curT] > cost:
            temperatures[curT] = cost
            ons[curT] = on
    
    for t in range(-10, 41):
        if temperatures[t] != -1:
            cost, curT, on = temperatures[t], t, ons[t]
            return_list.append([nextindex, cost, curT, on])
            
    return return_list
        

def BFS(temperature, t1, t2, a, b, onboard):
    # element: [index, cost, curT, on]
    que = deque()
    que.append([0, 0, temperature, False])
    
    for time in range(len(onboard) - 1):
        temp = []
        
        while len(que) > 0:
            currE = que.popleft()
            nextElements = nextAction(temperature, t1, t2, a, b, onboard, currE)
            temp += nextElements
            
        
        
        que = deque(check(temp, onboard, t1, t2))

    return que
    

def solution(temperature, t1, t2, a, b, onboard):
    answer = 0
    temp = BFS(temperature, t1, t2, a, b, onboard)
    temp = sorted([a[1] for a in list(temp)])

    return temp[0]