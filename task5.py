class Graph:
    def __init__(self):
        # Initialize an empty adjacency list
        self.adjacency_list = {}

    def add_edge(self, u, v):
        # Add an edge from vertex u to vertex v
        if u not in self.adjacency_list:
            self.adjacency_list[u] = []
        if v not in self.adjacency_list:
            self.adjacency_list[v] = []
        self.adjacency_list[u].append(v)
        self.adjacency_list[v].append(u)  # For undirected graph

    def bfs(self, start):
        # Perform Breadth-First Search (BFS) starting from the given vertex
        visited = set()  # Keep track of visited nodes
        queue = [start]  # Initialize the queue with the start node
        bfs_order = []  # List to store the order of traversal

        while queue:
            vertex = queue.pop(0)  # Dequeue a vertex
            if vertex not in visited:
                visited.add(vertex)  # Mark it as visited
                bfs_order.append(vertex)  # Add to the BFS order
                # Enqueue all unvisited neighbors
                queue.extend(neighbor for neighbor in self.adjacency_list[vertex] if neighbor not in visited)

        return bfs_order

    def dfs_recursive(self, vertex, visited=None):
        # Perform Depth-First Search (DFS) recursively
        if visited is None:
            visited = set()  # Initialize visited set
        visited.add(vertex)  # Mark the vertex as visited
        dfs_order = [vertex]  # List to store the order of traversal

        # Recur for all the neighbors
        for neighbor in self.adjacency_list[vertex]:
            if neighbor not in visited:
                dfs_order.extend(self.dfs_recursive(neighbor, visited))

        return dfs_order

    def dfs_iterative(self, start):
        # Perform Depth-First Search (DFS) iteratively
        visited = set()  # Keep track of visited nodes
        stack = [start]  # Initialize the stack with the start node
        dfs_order = []  # List to store the order of traversal

        while stack:
            vertex = stack.pop()  # Pop a vertex from the stack
            if vertex not in visited:
                visited.add(vertex)  # Mark it as visited
                dfs_order.append(vertex)  # Add to the DFS order
                # Push all unvisited neighbors onto the stack
                stack.extend(neighbor for neighbor in self.adjacency_list[vertex] if neighbor not in visited)

        return dfs_order

# Example usage
if __name__ == "__main__":
    g = Graph()
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(3, 5)

    print("BFS:", g.bfs(1))  # Output: BFS traversal starting from vertex 1
    print("DFS (Recursive):", g.dfs_recursive(1))  # Output: DFS traversal starting from vertex 1 (recursive)
    print("DFS (Iterative):", g.dfs_iterative(1))  # Output: DFS traversal starting from vertex 1 (iterative)