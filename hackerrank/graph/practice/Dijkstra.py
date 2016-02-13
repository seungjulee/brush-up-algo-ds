adj = {
    'A': set([('B', 20),('D', 80),('G',90)]),
    'B': set([('F', 10)]),
    'C': set([('H', 20)]),
    'D': set([('G', 20)]),
    'E': set([('G', 30), ('B',50)]),
    'F': set([('C', 10), ('D', 40)]),
    'G': set([('A', 20)]),
    'H': set([])
}
def shortest_dist_node(dist_so_far):
    return min(dist_so_far, key=dist_so_far.get)

def dijkstra(adj, s_vert):
    dist_so_far = {s_vert: 0}
    final_dist = {}
    while dist_so_far:
        u = shortest_dist_node(dist_so_far)
        final_dist[u] = dist_so_far[u]
        del dist_so_far[u]
        for v, weight in adj[u]:
            if v not in final_dist:
                if v not in dist_so_far:
                    dist_so_far[v] = final_dist[u] + weight
                elif final_dist[u] + weight < dist_so_far[v]:
                    dist_so_far[v] = final_dist[u] + weight
    if len(adj) is not len(final_dist):
        not_reachable = []
        for vertx in adj:
            if vertx not in final_dist:
                not_reachable.append(vertx)
        for vertx in not_reachable:
            final_dist[vertx] = "Not Reachable"
    return final_dist

print dijkstra(adj, 'A')














# class Graph(object):
#     def __init__(self):
#         self.vertexes = set()
#         self.edges = defaultdict(list)
#         self.weight = {}
#
#     def add_vertex(self, val):
#         self.vertexes.add(val)
#
#     def add_edge(self, from_vert, to_vert, weight):
#         self.edges[from_vert].append(to_vert)
#         self.edges[to_vert].append(from_vert)
#         self.weight[(from_vert, to_vert)] = weight
