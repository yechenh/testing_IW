# Depth-first search
def dfs(node, explored):
    if node in explored:
        return explored
    explored.append(node)
    for nei in node.neighbors:
        explored = dfs(nei, explored)
    return explored

# Breadth-first search
def bfs(start, goal):
    explored = []
    queue_paths = [[start]]
    while queue_paths:
        path = queue_paths[0]
        node = path[-1]
        queue_paths = queue_paths[1:]

        if node not in explored:
            explored.append(node)
            for nei in node.neighbors:
                new_path = list(path)
                new_path.append(nei)
                if nei == goal:
                    return new_path
                queue_paths.append(new_path)
                


