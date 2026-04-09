from collections import deque

# Function to perform BFS
def bfs(tree, root):
    visited = []          # To store visited nodes
    queue = deque([root]) # Initialize queue with root node

    while queue:
        node = queue.popleft()  # Dequeue a node
        visited.append(node)    # Mark it as visited

        # Add all children of the current node to the queue
        for child in tree.get(node, []):
            queue.append(child)

    return visited


# Example tree (Adjacency List representation)
tree = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': [],
    'D': ['G'],
    'E': [],
    'F': [],
    'G': []
}

# Run BFS starting from root node 'A'
result = bfs(tree, 'A')

# Display result
print("BFS Traversal Order:", result)
