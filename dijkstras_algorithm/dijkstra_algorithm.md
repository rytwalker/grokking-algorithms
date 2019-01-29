# Dijkstra's Algorithm

What is the sortest path to X?
Used for calculating the shortest path in a weighted graph.
only works with Directed Acyclic Graphs (DAG)
Negative weight edges break the algorithm (Bellman-Ford does this)

Steps:

1. Find the "cheapest" node.
2. Update the cost of the neighbors of this node.
3. Repeat until done for every node on graph.
4. Calculate final path.
