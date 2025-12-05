import networkx as nx
import matplotlib.pyplot as plt

def create_transport_network():
    """Create a graph of city metro/subway stations"""
    G = nx.Graph()
    
    # Add stations (nodes)
    stations = [
        "Central Station", "North Terminal", "South Terminal",
        "East Plaza", "West Park", "Airport",
        "University", "Hospital", "Mall", "Stadium"
    ]
    G.add_nodes_from(stations)
    
    # Add connections (edges)
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


if __name__ == "__main__":
    # Create graph
    G = create_transport_network()

    # ANALYSIS - Main characteristics
    print("=" * 50)
    print("GRAPH ANALYSIS")
    print("=" * 50)
    print(f"Number of stations (nodes): {G.number_of_nodes()}")
    print(f"Number of connections (edges): {G.number_of_edges()}")
    print(f"\nDegree of each station:")
    for node, degree in G.degree():
        print(f"  {node}: {degree} connections")

    # Additional characteristics
    print(f"\nAverage degree: {sum(dict(G.degree()).values()) / G.number_of_nodes():.2f}")
    print(f"Graph density: {nx.density(G):.3f}")

    # Visualize
    plt.figure(figsize=(12, 8))
    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=True, node_color='lightblue',
            node_size=3000, font_size=9, font_weight='bold',
            edge_color='gray', width=2)
    plt.title("City Transport Network")
    plt.axis('off')
    plt.tight_layout()
    plt.show()