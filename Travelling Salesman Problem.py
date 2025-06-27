def tsp(graph, s):
    n = len(graph)
    
    # Create adjacency list
    g = {i: [] for i in range(n)}
    for i in range(n):
        for j in range(n):
            if i != j and graph[i][j] != 0:
                g[i].append((j, graph[i][j]))

    min_cost = float('inf')
    stack = [(s, [s], 0)]  # (current node, path so far, current cost)

    while stack:
        curr, path, cost = stack.pop()
        if len(path) == n:
            for neighbour, weight in g[curr]:
                if neighbour == s:
                    total_cost = cost + weight
                    min_cost = min(min_cost, total_cost)
                    break
        else:
            for neighbour, weight in g[curr]:
                if neighbour not in path:
                    stack.append((neighbour, path + [neighbour], cost + weight))
    
    return min_cost

# Input graph (cost matrix)
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

s = 0  # starting city
print("Minimum TSP Cost:", tsp(graph, s))
