from collections import namedtuple, deque
import random

inf = float('inf')
Edge = namedtuple('Edge', ['start', 'end', 'cost'])

class Graph():
    def __init__(self, edges):
        self.edges = [Edge(*edge) for edge in edges]
        self.vertices = {e.start for e in self.edges} | {e.end for e in self.edges}

    def dijkstra(self, source, dest):
        assert source in self.vertices
        dist = {vertex: inf for vertex in self.vertices}
        previous = {vertex: None for vertex in self.vertices}
        dist[source] = 0
        q = self.vertices.copy()
        neighbours = {vertex: set() for vertex in self.vertices}
        for start, end, cost in self.edges:
            neighbours[start].add((end, cost))
            neighbours[end].add((start, cost))

        while q:
            u = min(q, key=lambda vertex: dist[vertex])
            q.remove(u)
            if dist[u] == inf or u == dest:
                break
            for v, cost in neighbours[u]:
                alt = dist[u] + cost
                if alt < dist[v]:
                    dist[v] = alt
                    previous[v] = u

        s, u = deque(), dest
        while previous[u]:
            s.appendleft(u)
            u = previous[u]
        s.appendleft(u)
        return s

if __name__ == "__main__":
    # Generate a random graph with 1000 nodes and random edges
    num_nodes = 1000
    nodes = [f"Node_{i}" for i in range(num_nodes)]
    edges = []

    for _ in range(5000):  # Random edges between nodes, approximately 5000 edges
        start, end = random.sample(nodes, 2)  # Pick two distinct nodes
        cost = random.randint(1, 100)  # Random cost between 1 and 100
        edges.append((start, end, cost))

    graph = Graph(edges)

    # Random start and destination nodes
    start_node = random.choice(nodes)
    dest_node = random.choice(nodes)

    # Run Dijkstra's algorithm
    graph.dijkstra(start_node, dest_node)
