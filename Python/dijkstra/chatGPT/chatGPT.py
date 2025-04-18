import heapq
import random

def dijkstra(graph, start):
    # Priority queue to hold (cost, node)
    pq = [(0, start)]
    # Dictionary to hold the shortest path to each node
    shortest_paths = {start: (None, 0)}
    visited = set()

    while pq:
        current_cost, current_node = heapq.heappop(pq)

        if current_node in visited:
            continue

        visited.add(current_node)

        for neighbor, weight in graph[current_node].items():
            cost = current_cost + weight

            if neighbor not in shortest_paths or cost < shortest_paths[neighbor][1]:
                shortest_paths[neighbor] = (current_node, cost)
                heapq.heappush(pq, (cost, neighbor))

    return shortest_paths

if __name__ == "__main__":
    # Generate a random graph with 1000 nodes
    num_nodes = 1000
    nodes = [f"Node_{i}" for i in range(num_nodes)]
    graph = {node: {} for node in nodes}

    # Add random edges with weights
    for node in nodes:
        num_edges = random.randint(1, 10)  # Each node has 1 to 10 neighbors
        neighbors = random.sample(nodes, num_edges)
        for neighbor in neighbors:
            if neighbor != node:
                graph[node][neighbor] = random.randint(1, 100)  # Random weight between 1 and 100

    # Select a random start node
    start_node = random.choice(nodes)
    # Run Dijkstra's algorithm
    dijkstra(graph, start_node)
