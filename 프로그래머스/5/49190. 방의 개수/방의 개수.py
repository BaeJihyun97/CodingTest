from collections import deque
from copy import deepcopy

def dfs(graph, start, nodes):
    stack = deque()
    stack.append(start)
    visited = [False]*nodes
    parent = [-1]*nodes
    visitime = [-1]*nodes
    simple_cycle = 0
    timer = 0
    
    while len(stack) > 0:
        curr = stack.pop()
        
        if visited[curr]:
            continue
            
        visited[curr] = True
        visitime[curr] = timer
        timer += 1
        
        for adj_node in graph[curr]:

            if not visited[adj_node]:
                
                parent[adj_node] = curr
                stack.append(adj_node)
            else:
                if parent[curr] != adj_node and visitime[adj_node] < visitime[curr]:
                    simple_cycle += 1

    return simple_cycle

def solution(arrows):
    answer, answer2 = 0, 0
    
    # making graph
    nodes = {(0, 0): 0}
    directions = {0:(0, 1), 1:(1, 1), 2:(1, 0), 3:(1, -1), 4:(0, -1), 5:(-1, -1), 6:(-1, 0), 7:(-1, 1)}
    graph = [[]]
    diagonal = {1:(1, -1), 3:(1, -1), 5:(-1, 1), 7:(-1, 1)}
    
    prev_node = (0, 0)
    for arrow in arrows:
        direction = directions[arrow]
        next_node =  (direction[0] + prev_node[0], direction[1] + prev_node[1])
        new_node = False
        new_edge = False
        
        # 새로운 노드일 때
        if next_node not in nodes.keys():
            nodes[next_node] = len(nodes)
            graph.append([])
            new_node = True
        
        # 새로운 엣지일 때
        if nodes[prev_node] not in graph[nodes[next_node]]:
            graph[nodes[next_node]].append(nodes[prev_node])
            graph[nodes[prev_node]].append(nodes[next_node])
            new_edge = True
            if not new_node:
                answer2 += 1
                # print(graph, nodes[next_node], nodes[prev_node])
            

        
        # 대각선 교점 발생시 교점을 노드로 만들기
        if arrow in [1, 3, 5, 7] and new_edge:
            temp1, temp2 = deepcopy(prev_node), deepcopy(next_node)
            center = ((temp1[0]+temp2[0]) / 2, (temp1[1]+temp2[1]) / 2)
            temp3 = (temp1[0]+diagonal[arrow][0], temp1[1])
            temp4 = (temp2[0]+diagonal[arrow][1], temp2[1])
            
            if center in nodes.keys():
                graph[nodes[next_node]].remove(nodes[prev_node])
                graph[nodes[prev_node]].remove(nodes[next_node])

            elif temp3 in nodes.keys() and temp4 in nodes.keys() and nodes[temp4] in graph[nodes[temp3]]:
                t1, t2, t3, t4 = nodes[temp1], nodes[temp2], nodes[temp3], nodes[temp4]
                answer2 += 1

                graph[t3].remove(t4); graph[t4].remove(t3);
                graph[t1].remove(t2); graph[t2].remove(t1);

                nodes[center] = len(nodes)
                c = nodes[center]
                graph.append([])

                graph[c].append(t1); graph[t1].append(c);
                graph[c].append(t2); graph[t2].append(c);
                graph[c].append(t3); graph[t3].append(c);
                graph[c].append(t4); graph[t4].append(c);
                
                


        prev_node = next_node
    
    # print(graph)
    vertex = len(nodes)
    edge = sum([len(g) for g in graph]) // 2
    answer = 1 + edge - vertex
    # answer = dfs(graph, 0, len(nodes))
    # print(answer2)
        
    return answer