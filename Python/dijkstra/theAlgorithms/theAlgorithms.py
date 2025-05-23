import heapq
import random

def dijkstra(graph, start, end):
    """Return the cost of the shortest path between vertices start and end."""
    heap = [(0, start)]  # cost from start node, end node
    visited = set()
    while heap:
        (cost, u) = heapq.heappop(heap)
        if u in visited:
            continue
        visited.add(u)
        if u == end:
            return cost
        for v, c in graph[u]:
            if v in visited:
                continue
            next_item = cost + c
            heapq.heappush(heap, (next_item, v))
    return -1

# Random graph generation for 1000 nodes and random edges
num_nodes = 1000
nodes = [f"Node_{i}" for i in range(num_nodes)]
graph = {}

# Generate random edges for the graph
for node in nodes:
    graph[node] = []
    num_edges = random.randint(1, 5)  # Each node will have 1 to 5 edges
    for _ in range(num_edges):
        neighbor = random.choice(nodes)
        if neighbor != node:
            cost = random.randint(1, 100)  # Random cost between 1 and 100
            graph[node].append((neighbor, cost))

# Random start and destination nodes
start_node = random.choice(nodes)
dest_node = random.choice(nodes)

# Run Dijkstra's algorithm
shortest_distance = dijkstra(graph, start_node, dest_node)

# If you want to check the result
# print(f"Shortest distance from {start_node} to {dest_node} is {shortest_distance}")
