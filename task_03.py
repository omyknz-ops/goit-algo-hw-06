import networkx as nx
import matplotlib.pyplot as plt

#Create a weighted graph - distances in km between stations
def create_weighted_transport_network():
    G = nx.Graph()
    
    stations = [
        "Central Station", "North Terminal", "South Terminal",
        "East Plaza", "West Park", "Airport",
        "University", "Hospital", "Mall", "Stadium"
    ]
    G.add_nodes_from(stations)
    
    # Add weighted edges (station1, station2, distance_in_km)
    weighted_connections = [
        ("Central Station", "North Terminal", 5),
        ("Central Station", "South Terminal", 4),
        ("Central Station", "East Plaza", 3),
        ("Central Station", "West Park", 6),
        ("North Terminal", "Airport", 8),
        ("North Terminal", "University", 4),
        ("South Terminal", "Hospital", 3),
        ("South Terminal", "Mall", 5),
        ("East Plaza", "Stadium", 2),
        ("East Plaza", "Mall", 4),
        ("West Park", "University", 3),
        ("West Park", "Hospital", 7),
        ("Airport", "Stadium", 6),
        ("University", "Hospital", 2),
        ("Mall", "Stadium", 3)
    ]
    
    for station1, station2, weight in weighted_connections:
        G.add_edge(station1, station2, weight=weight)
    
    return G

# Create weighted graph
G = create_weighted_transport_network()

# Visualize with weights
plt.figure(figsize=(14, 10))
pos = nx.spring_layout(G, seed=42)
nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=3000)
nx.draw_networkx_labels(G, pos, font_size=9, font_weight='bold')
nx.draw_networkx_edges(G, pos, edge_color='gray', width=2)

# Draw edge labels (weights)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels, font_size=8)

plt.title("Weighted City Transport Network (distances in km)")  
plt.axis('off')  
plt.tight_layout() 
plt.show()  

# Find shortest paths between ALL vertices using Dijkstra's algorithm
print("=" * 70) 
print("SHORTEST PATHS BETWEEN ALL STATIONS (Dijkstra's Algorithm)")  
print("=" * 70) 

all_paths = dict(nx.all_pairs_dijkstra(G, weight='weight'))

for start, (distances, paths) in all_paths.items():
    print(f"\n--- From {start} ---")
    for end, path in paths.items():
        if start != end:
            distance = distances[end]
            path_str = " -> ".join(path)
            print(f"  To {end}: {path_str} ({distance} km)")