# Depth-First Search (DFS) for a Tree

def dfs(tree, node, visited):
    visited.append(node)   # Visit the node

    for child in tree[node]:   # Visit all children
        dfs(tree, child, visited)

    return visited


# Predefined tree
tree = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': [],
    'D': ['G'],
    'E': [],
    'F': [],
    'G': []
}

# Start from root
root = 'A'

# Perform DFS
result = dfs(tree, root, [])

# Output
print("DFS Traversal Order:", result)
