"""6. Write a Program to check if a given graph is a complete graph. Represent the 
graph using the Adjacency Matrix representation."""
class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_matrix = [[0] * vertices for _ in range(vertices)]

    def add_edge(self, u, v):
        self.adj_matrix[u][v] = 1
        self.adj_matrix[v][u] = 1

    def is_complete(self):
        for i in range(self.vertices):
            for j in range(self.vertices):
                if i != j and self.adj_matrix[i][j] == 0:
                    return False
        return True
    def mat(self):
        return self.adj_matrix


# Example usage
if __name__ == "__main__":
    num_vertices = 5
    g = Graph(num_vertices)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(0, 3)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 3)
    print(g.mat())
    if g.is_complete():
        print("The graph is a complete graph.")
    else:
        print("The graph is not a complete graph.")
