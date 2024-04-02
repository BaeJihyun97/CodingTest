from bisect import bisect_left

# def binarySearch(array, value):
#     start, end = 0, len(array) -1
#     index = (end + start) // 2
    
#     count = 0
#     while start < end:
#         midum = array[index]
#         if midum == value:
#             # 값이 중복인 것이 있을 수 있음
#             while True:
#                 if index > 0 and array[index-1]==midum: index -= 1
#                 else: break
#             break
#         elif midum > value:
#             end = index
#         else: # midum < value
#             if start == index: # 값이 없을 때 큰 수 중 가장 가까운 수 index 반환
#                 index += 1
#                 break
#             else:
#                 start = index
        
#         index = (end + start) // 2
#     return index
            

def find(info_tables, lang, job, career, food, score):
    count = 0
    info_table = info_tables[(lang, job, career, food)]
    index = bisect_left(info_table, score)
    
    return len(info_table) - index

def solution(info, query):
    answer = []
    info_table = []
    query_table = []
    convert_dict = {"cpp":1, "java":2, "python":3, "backend":1, "frontend":2, "junior":1, "senior":2, "chicken":1, "pizza":2, "-":0}
    for inf in info:
        temp = inf.split(" ")
        temp[-1] = int(temp[-1])
        temp = [convert_dict[q] if not isinstance(q, int) else q for q in temp]
        info_table.append(temp)
        
    for quer in query:
        temp = [q for q in quer.split(" ") if q != "and"]
        temp[-1] = int(temp[-1])
        temp = [convert_dict[q] if not isinstance(q, int) else q for q in temp]
        query_table.append(temp)
        
    info_table.sort(key=lambda x : x[-1])

    
    info_tables = {}
    # 모든 경우의 수 미리 인덱싱 해놓기. 몇개 안되니까^^ l, j, c, f, s
    for lang in range(4):
        for job in range(3):
            for career in range(3):
                for food in range(3):
                    key = (lang, job, career, food)
                    temp = []
                    for [l, j, c, f, s] in info_table:
                        if (lang == 0 or lang == l) and (job == 0 or job == j) and (career==0 or career == c) and (food==0 or food==f):
                            temp.append(s)
                    info_tables[key] = temp
    
    for query in query_table:
        answer.append(find(info_tables, *query))
    
    # temp = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7]
    # print(len(temp) - binarySearch(temp, 2))
        
    
    return answer