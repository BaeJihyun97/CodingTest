from datetime import datetime, timedelta

def solution(lines):
    times_end = []
    times_start = []
    
    
    for line in lines:
        time = line.split(" ")
        endTime = datetime.strptime(time[0] + " " + time[1], '%Y-%m-%d %H:%M:%S.%f')
        durTime = timedelta(milliseconds=int(float(time[2][:-1])*1000) - 1)
        strTime = endTime - durTime

        times_end.append(endTime)
        times_start.append(strTime)

    delta = timedelta(milliseconds=999)
    count = 0
    for index, (start, end) in enumerate(zip(times_start, times_end)):
        temp = 0
        for s in times_start[index:]:
            if s <= end+delta: temp += 1
            
        count = max(count, temp)
        
        
        
    return count