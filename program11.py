def is_safe(node, color, assignment, graph):
    for neighbor in graph[node]:
        if assignment.get(neighbor) == color:
            return False
    return True
def map_coloring(graph, colors, assignment={}):
    if len(assignment) == len(graph):
        print("Solution:", assignment)
        return True
    unassigned = [n for n in graph if n not in assignment][0]
    for color in colors:
        if is_safe(unassigned, color, assignment, graph):
            assignment[unassigned] = color
            if map_coloring(graph, colors, assignment):
                return True
            del assignment[unassigned]
    return False
graph = {
    'WA': ['NT','SA'],
    'NT': ['WA','SA','Q'],
    'SA': ['WA','NT','Q','NSW','V'],
    'Q': ['NT','SA','NSW'],
    'NSW': ['Q','SA','V'],
    'V': ['SA','NSW'],
    'T': []
}
colors = ['Red','Green','Blue']
map_coloring(graph, colors)
