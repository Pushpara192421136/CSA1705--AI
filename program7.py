from collections import deque
def bfs(graph, start):
    visited = set([start])
    q = deque([start])
    while q:
        node = q.popleft()
        print(node, end=" ")
        for n in graph[node]:
            if n not in visited:
                visited.add(n)
                q.append(n)
graph = {
    'A': ['B','C'],
    'B': ['D','E'],
    'C': ['F'],
    'D': [], 'E': ['F'], 'F': []
}
bfs(graph, 'A')
