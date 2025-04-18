import heapq
import random

def dijkstra(graph, start):
    """
    Dijkstra's Algorithm: finds the shortest path from `start` to all other nodes in `graph`

    Args:
        graph: a dictionary of adjacency lists, where each key is a node and each value is a list of tuples (neighbor, weight)
        start: the starting node

    Returns:
        A dictionary of shortest distances from `start` to all other nodes, and a dictionary of predecessors
    """
    # Initialize distances and predecessors
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    predecessors = {node: None for node in graph}

    # Priority queue of nodes to visit, with their distances
    queue = [(0, start)]

    while queue:
        # Extract the node with the minimum distance from the queue
        current_distance, current_node = heapq.heappop(queue)

        # If we've already processed this node, skip it
        if current_distance > distances[current_node]:
            continue

        # Visit all neighbors of the current node
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            # If we've found a shorter path to the neighbor, update its distance and predecessor
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))

    return distances, predecessors

if __name__ == "__main__":
    # Generate a random graph with 1000 nodes
    num_nodes = 1000
    nodes = [f"Node_{i}" for i in range(num_nodes)]
    graph = {node: [] for node in nodes}

    # Add random edges with weights
    for node in nodes:
        num_edges = random.randint(1, 10)  # Each node has 1 to 10 neighbors
        neighbors = random.sample(nodes, num_edges)
        for neighbor in neighbors:
            if neighbor != node:
                graph[node].append((neighbor, random.randint(1, 100)))  # Random weight between 1 and 100

    # Select a random start node
    start_node = random.choice(nodes)
    # Run Dijkstra's algorithm
    dijkstra(graph, start_node)
