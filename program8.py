def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=" ")
    for n in graph[start]:
        if n not in visited:
            dfs(graph, n, visited)
graph = {
    'A': ['B','C'],
    'B': ['D','E'],
    'C': ['F'],
    'D': [], 'E': ['F'], 'F': []
}
dfs(graph, 'A')
