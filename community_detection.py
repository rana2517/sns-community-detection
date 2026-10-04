import networkx as nx
import community as community_louvain
import matplotlib.pyplot as plt

# Load sample social network graph (Zachary's Karate Club)
G = nx.karate_club_graph()

print(f"[+] Graph loaded: {G.number_of_nodes()} nodes, {G.number_of_edges()} edges\n")

# Detect communities using Louvain method
partition = community_louvain.best_partition(G)

# Print which community each node belongs to
print("[+] Community assignments:")
for node, comm_id in partition.items():
    print(f"    Node {node} -> Community {comm_id}")

# Number of communities found
num_communities = len(set(partition.values()))
print(f"\n[+] Total communities detected: {num_communities}")

# Modularity score (how well-separated the communities are)
modularity = community_louvain.modularity(partition, G)
print(f"[+] Modularity score: {modularity:.4f}")

# Visualize
pos = nx.spring_layout(G, seed=42)
cmap = plt.colormaps.get_cmap('viridis').resampled(num_communities)
nx.draw(G, pos, node_color=list(partition.values()), cmap=cmap,
        with_labels=True, node_size=500, font_color='white', font_weight='bold')
plt.title(f"Community Detection - Zachary's Karate Club\n({num_communities} communities, modularity={modularity:.3f})")
plt.savefig("communities.png", dpi=150, bbox_inches='tight')
print("\n[+] Graph saved as communities.png")
plt.show()
