from collections import deque

def solution(edges):
    # make graph
    NODE = max([ed for edge in edges for ed in edge])
    graph = [[] for _ in range(NODE+1)]
    isInit = [True]*(NODE+1)
    visited = {tuple(key):False for key in edges}
    for [start, end] in edges:
        graph[start].append(end)
        isInit[end] = False
    
    # find init node
    MAX = 0
    init = 0
    for i in range(1, NODE):
        if isInit[i]:
            linkedNode = len(graph[i])
            if MAX < linkedNode:
                MAX = linkedNode
                init = i

    # print(graph, isInit)
    # count graph
    type0, type1, type2 = 0, 0, 0 # 막대, 도넛, 팔자
    for i, nodes in enumerate(graph):
        if i != init and i != 0:
            if len(nodes) == 2:
                type2 += 1
            elif len(nodes) == 0:
                type0 += 1
    
    # print(type0, type1, type2)
    type1 = len(graph[init]) - type0 - type2
    answer = [init, type1, type0, type2]
    return answer

# 그래프 순회 오류남....
#     for node in graph[init]:
#         stack = deque([(init, node)])
#         flag = False
        
#         while len(stack) > 0:
#             currE = stack.pop()
#             if visited[currE] == True:
#                 continue
#             visited[currE] = True
#             (start, end) = currE
            
#             if not flag:
#                 if len(graph[end]) == 2:
#                     type2 += 1
#                     flag = True
#                 elif len(graph[end]) == 0:
#                     type0 += 1
#                     flag = True
                
#             for next_node in graph[end]:
#                 if not visited[(end, next_node)]:
#                     stack.append((end, next_node))

#         if not flag:
#             type1 += 1