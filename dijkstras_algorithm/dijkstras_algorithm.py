# Dijkstra's Algorithm

graph = {}
costs = {}
parents = {}

# Add verts and weights to graph
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2
graph["a"] = {}
graph["a"]["fin"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5
graph["fin"] = {}

# costs hash table
infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

# parents hash table
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

processed = set()

node = find_lowest_node(costs)
# while we have nodes to process
while node:
    # grab the node that's closest to the start
    cost = costs[node]
    neighbors = graph[node]
    # update costs for its neighbors
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        # if any neightbors' costs were updated, update parents' too
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    # mark this node processed
    processed.add(node)
    node = find_lowest_node(node)
