import networkx as nx
import matplotlib.pyplot as plt

# Create a graph representing a city transportation network
def create_transport_network():
    G = nx.Graph()
    
    # Add stations (nodes)
    stations = [
        "Central Station",
        "North Terminal",
        "South Terminal",
        "East Plaza",
        "West Park",
        "Airport",
        "University",
        "Hospital",
        "Mall",
        "Stadium"
    ]
    
    G.add_nodes_from(stations)
    
    # Add connections (edges) between stations
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


# Create graph
G = create_transport_network()

# Visualize
plt.figure(figsize=(12, 8))
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_color='lightblue', 
        node_size=3000, font_size=10, font_weight='bold', 
        edge_color='gray', width=2)
plt.title("City Transport Network")
plt.axis('off')
plt.tight_layout()
plt.show()