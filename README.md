# Tools for Detecting Communities in Social Networks

A Python-based implementation of community detection in social network graphs using the Louvain algorithm, with discussion of social network infrastructure and big data privacy implications.

## Overview
Social networks can be modeled as graphs where nodes represent individuals and edges represent connections. This project detects densely connected sub-groups (communities) within such a graph and evaluates how well-separated those communities are using the modularity metric.

## Tools & Technologies
- Python 3
- NetworkX (graph construction and analysis)
- python-louvain (Louvain community detection algorithm)
- Matplotlib (graph visualization)

## Dataset
Zachary's Karate Club — a classic 34-node, 78-edge social network dataset widely used to benchmark community detection algorithms.

## How It Works
1. Load the social network graph using NetworkX
2. Apply the Louvain method to partition nodes into communities
3. Calculate the modularity score to evaluate community structure quality
4. Visualize the graph with nodes colored by detected community

## Usage
```bash
pip install networkx matplotlib python-louvain --break-system-packages
python3 community_detection.py
```

## Results
- **Nodes:** 34, **Edges:** 78
- **Communities detected:** 4
- **Modularity score:** 0.4439 (indicates well-separated community structure)

## Social Network Infrastructure
Large-scale platforms (Facebook, Twitter) store graph data using distributed Big Data infrastructure (e.g., Hadoop, Spark GraphX) to run community detection at billions-of-nodes scale.

## Big Data & Privacy
Community detection can expose sensitive information through de-anonymization, even when user data is anonymized. Mitigation techniques include k-anonymity and differential privacy to protect individual identities while preserving analytical value.

## Author
Rajesh Kumar — B.E. Computer Science & Cyber Security,
