
# def DFS(adj):
#     stack = []
adj_topo_example = {
    '0': [],
    '1': [],
    '2': ['3'],
    '3': ['1'],
    '4': ['0','1'],
    '5': ['0','2']
}
adj = {'A': ['B', 'D', 'G'],
       'B': ['A', 'E', 'F'],
       'C': ['F', 'H'],
       'D': ['A', 'F'],
       'E': ['B', 'G'],
       'F': ['B', 'C', 'D'],
       'G': ['A', 'E'],
       'H': ['C']}


def DFS_iter(adj, s):
    visited, stack = [],[s]
    while stack:
        u = stack.pop()
        if u not in visited:
            visited.append(u)
            stack = stack + [ v for v in sorted(adj[u]) if v not in visited]
    return visited

def DFS_visit(adj, u, visited):
    visited.append(u)
    for v in adj[u]:
        if v not in visited:
            DFS_visit(adj, v, visited)

def DFS_all(adj, s):
    visited = []
    DFS_visit(adj, s, visited)
    for u in adj:
        if u not in visited:
            DFS_visit(adj, u, visited)

    return visited
def topological_sort_visit(adj, u, stack, visited):
    visited.append(u)
    for v in adj[u]:
        if v not in visited:
            topological_sort_visit(adj, v, stack, visited)
    stack.append(u)
def topological_sort(adj):
    stack, visited = [], []

    for u in adj:
        if u not in visited:
            topological_sort_visit(adj, u, stack, visited)


print topological_sort(adj_topo_example)

# print DFS_all(adj_topo_example, '5')

# def BFS(adj, s):
#     level = {s: 0}
#     parent = {s: None}
#     frontier = [s]
#     path = [s]
#     i = 1
#
#     while frontier:
#         next_frontier = []
#         for u in frontier:
#             next_frontier.append(u)
#             for v in adj[u]:
#                 if v not in parent:
#                     parent[v] = u
#                     level[v] = i
#                     next_frontier.append(v)
#                     path.append(v)
#         i += 1
#         frontier = next_frontier
#
#     return path

def BFS(adj,s):
    level = {s: 0}
    parent = {s: None}
    i = 1
    frontier = [s]
    visited_print = [s]
    while frontier:
        next_frontier = []
        for u in frontier:
            for v in adj[u]:
                if v not in level:
                    level[v] = i
                    parent[v] = u
                    next_frontier.append(v)
                    visited_print.append(v)
        frontier = next_frontier
        i += 1
    return visited_print, level, parent









# print DFS_all(adj_topo_example, '5')
# print list(DFS_path(adj_topo_example, '5','1'))







# def DFS(adj, s):
#     parent = {}
#
#     for u in adj:
#         if u not in parent:
#             parent[u] = None
#             DFS_visit(adj, u, parent)
#
#     print parent
#
# def DFS_visit(adj, u, parent):
#     for v in adj[u]:
#         if v not in parent:
#             parent[v] = u
#             DFS_visit(adj, v, parent)
# adj = {'A': ['B', 'D', 'G'],
#        'B': ['A', 'E', 'F'],
#        'C': ['F', 'H'],
#        'D': ['A', 'F'],
#        'E': ['B', 'G'],
#        'F': ['B', 'C', 'D'],
#        'G': ['A', 'E'],
#        'H': ['C']}

# print BFS('A', adj)
