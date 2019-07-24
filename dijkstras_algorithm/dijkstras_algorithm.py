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

'''
graph {
    start: {a: 6, b: 2},
    a: {fin: 1}
    b: {a: 3, fin: 5}
    fin: {}
}
'''

# costs hash table
infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity


'''
costs: {a: 6, b: 2, fin: infinity}
'''

# parents hash table
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

'''
parents: {a: "start", b: "start", fin: None}
'''

processed = set()


def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
        return lowest_cost_node


node = find_lowest_cost_node(costs)
# while we have nodes to process
while node:
    # grab the node that's closest to the start
    cost = costs[node]  # 2 5
    neighbors = graph[node]  # {a: 3, fin: 5} {fin: 1}
    # update costs for its neighbors
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]  # 5 7 6
        # if any neightbors' costs were updated, update parents' too
        if costs[n] > new_cost:
            costs[n] = new_cost  # {a: 5} {fin: 7} {fin: 6}
            parents[n] = node  # {a: 'b'} {fin: b} {fin: a}
    # mark this node processed
    processed.add(node)
    node = find_lowest_cost_node(node)
