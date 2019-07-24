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


1. Find the "cheapest" node.
   1. POSTER 0
   2. LP 5
   3. DRUM SET 20
   4. BASS 15
   5. PIANO 10
2. Update the cost of the neighbors of this node.
3. Repeat until done for every node on graph.
4. Calculate final path.

## 3 Hashtables for Dijkstra's Algorithm
1. Graph
2. Costs
3. Parents