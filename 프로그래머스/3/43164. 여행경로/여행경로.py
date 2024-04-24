from itertools import chain


def dfs(node, edges, visited, graph, depth, r, path):
    if depth == r:
        return path
    
    tpath = ["ZZZ" for _ in range(r+1)]
    for nextNode in graph[node]:
        if visited[(node, nextNode)] > 0:
            visited[(node, nextNode)] -= 1
            temp = dfs(nextNode, edges, visited, graph, depth+1, r, path+[nextNode])
            # print(depth, tpath, temp, visited)
            if len(temp) == r+1 and "".join(tpath) > "".join(temp):
                tpath = temp
            visited[(node, nextNode)] += 1

    return tpath

def solution(tickets):
    answers = []
    nodes = list(set(chain.from_iterable(tickets)))
    graph = {node:[] for node in nodes}
    
    for [node1, node2] in tickets:
        graph[node1].append(node2)
    
    for g in graph:
        graph[g].sort(reverse=True)
        
    visited = {(t[0], t[1]):tickets.count(t) for t in tickets}
    answer = dfs("ICN", tickets, visited, graph, 0, len(tickets), ["ICN"])
    return answer