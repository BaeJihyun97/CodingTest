from collections import deque

def countDiff1(string1, string2):
    count = 0
    for s1, s2 in zip(string1, string2):
        if s1 != s2:
            count += 1
        
    return (count==1)

def bfs(begin, target, graph):
    if len(graph[target]) == 0:
        return 0
    
    que = deque()
    count = 0
    maxCount = len(graph)
    visited = [False for _ in range(len(graph))]
    flag = False
    
    que.append(begin)
    while count < maxCount:
        temp = []
        
        while len(que) > 0:
            curr = que.popleft()
            
            if curr == target:
                flag = True
                break
                
            elif not visited[curr]:
                visited[curr] == True
                
                for nextNode in graph[curr]:
                    if not visited[nextNode]:
                        temp.append(nextNode)
        
        if flag:
            break
        else:
            que.clear()
            que.extend(temp)
            count += 1
    
    if flag:
        return count
    else:
        return 0
                
    


def solution(begin, target, words):
    answer = 0
    
    # graph 만들기
    nodes = {key:i for i, key in enumerate(set([begin, target]+words))}
    graph = [[] for _ in range(len(nodes))]
    temp = list(set([begin] + words))
    
    for i, node1 in enumerate(temp):
        for node2 in temp[i:]:
            if countDiff1(node1, node2):
                graph[nodes[node1]].append(nodes[node2])
                graph[nodes[node2]].append(nodes[node1])
    
    # bfs
    return bfs(nodes[begin], nodes[target], graph)