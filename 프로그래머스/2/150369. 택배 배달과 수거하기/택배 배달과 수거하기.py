def solution(cap, n, deliveries, pickups):
    answer = 0
    index = n-1
    indexP = n-1
    count = 0
    while index >= 0 or indexP >= 0:
        truck = 0
        farest = -1
        while truck < cap and index >= 0:
            delivery = deliveries[index]
            if delivery != 0 and index > farest:
                farest = index
            if cap - truck >= delivery:
                truck += delivery
                deliveries[index] = 0
                index -= 1
            else:
                deliveries[index] -= cap - truck
                truck = cap
                break
                
        truck = 0
        while truck < cap and indexP >= 0:
            pickup = pickups[indexP]
            if pickup != 0 and indexP > farest:
                farest = indexP
            if cap - truck >= pickup:
                truck += pickup
                pickups[indexP] = 0
                indexP -= 1
            else:
                pickups[indexP] -= cap - truck
                truck = cap
                break
        
        answer += (farest+1)*2
        
    
    return answer