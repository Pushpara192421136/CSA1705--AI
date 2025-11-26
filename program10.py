from heapq import heappush, heappop
def a_star(start, goal, graph, h):
    pq = [(h[start], 0, start, [start])]
    visited = set()
    while pq:
        f, g, node, path = heappop(pq)
        if node == goal:
            print("Path:", path)
            print("Cost:", g)
            return
        if node in visited:
            continue
        visited.add(node)
        for neighbor, cost in graph[node].items():
            if neighbor not in visited:
                heappush(pq, (g + cost + h[neighbor], g + cost, neighbor, path + [neighbor]))
graph = {
    'A': {'B':1,'C':4},
    'B': {'C':2,'D':5},
    'C': {'D':1},
    'D': {}
}
heuristic = {'A':7, 'B':6, 'C':2, 'D':0}
a_star('A', 'D', graph, heuristic)
