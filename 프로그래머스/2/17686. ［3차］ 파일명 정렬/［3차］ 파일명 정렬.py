def split3(string: str, order: int) -> tuple:
    # find head
    index = []
    maxL = len(string)
    
    for i in range(maxL):
        if ord(string[i]) >= 48 and ord(string[i]) <= 57:
            index.append(i)
            break
    for i in range(index[-1], maxL):
        if ord(string[i]) < 48 or ord(string[i]) > 57:
            index.append(i)
            break
        if i == maxL - 1:
            index.append(maxL)
            
    splited = (string[0:index[0]].lower(), int(string[index[0]:index[1]]), order, string)
    return splited
        
           

def solution(files):
    answer = []
    for i, f in enumerate(files):
        answer.append(split3(f, i))
        
    answer.sort(key = lambda x : (x[0], x[1], x[2]))
    answer = [a[3] for a in answer]
    return answer