import networkx as nx
import matplotlib.pyplot as plt

#Create a graph of city metro/subway stations
def create_transport_network():
    G = nx.Graph()
    
    stations = [
        "Central Station", "North Terminal", "South Terminal",
        "East Plaza", "West Park", "Airport",
        "University", "Hospital", "Mall", "Stadium"
    ]
    G.add_nodes_from(stations)
    
    connections = [
        ("Central Station", "North Terminal"),
        ("Central Station", "South Terminal"),
        ("Central Station", "East Plaza"),
        ("Central Station", "West Park"),
        ("North Terminal", "Airport"),
        ("North Terminal", "University"),
        ("South Terminal", "Hospital"),
        ("South Terminal", "Mall"),
        ("East Plaza", "Stadium"),
        ("East Plaza", "Mall"),
        ("West Park", "University"),
        ("West Park", "Hospital"),
        ("Airport", "Stadium"),
        ("University", "Hospital"),
        ("Mall", "Stadium")
    ]
    G.add_edges_from(connections)
    
    return G

# Depth-First Search - explores as far as possible along each branch
def dfs_path(graph, start, goal, path=None):
    if path is None:
        path = []
    
    path = path + [start]
    
    if start == goal:
        return path
    
    for neighbor in graph.neighbors(start):
        if neighbor not in path:  # Avoid cycles
            new_path = dfs_path(graph, neighbor, goal, path)
            if new_path:
                return new_path
    
    return None

# Breadth-First Search - explores all neighbors at the present depth prior to moving on to nodes at the next depth level
def bfs_path(graph, start, goal):
    queue = [(start, [start])]  # Queue of (node, path_to_node)
    visited = set()
    
    while queue:
        current, path = queue.pop(0)  # Get first element (FIFO)
        
        if current == goal:
            return path
        
        if current in visited:
            continue
        
        visited.add(current)
        
        for neighbor in graph.neighbors(current):
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))
    
    return None


# Create graph
G = create_transport_network()

# Test algorithms
start = "Central Station"
goal = "Stadium"

print("=" * 60)
print(f"Finding path from '{start}' to '{goal}'")
print("=" * 60)

dfs_result = dfs_path(G, start, goal)
print(f"\nDFS Path: {' -> '.join(dfs_result)}")
print(f"DFS Path length: {len(dfs_result)} stations")

bfs_result = bfs_path(G, start, goal)
print(f"\nBFS Path: {' -> '.join(bfs_result)}")
print(f"BFS Path length: {len(bfs_result)} stations")

print("\n" + "=" * 60)
print("COMPARISON")
print("=" * 60)
print(f"DFS found path with {len(dfs_result)} stations")
print(f"BFS found path with {len(bfs_result)} stations")