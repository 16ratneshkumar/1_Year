"""7. Write a Program to check if a given graph is a complete graph. Represent the 
graph using the Adjacency List representation."""
class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = [[] for _ in range(vertices)]

    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def is_complete(self):
        for i in range(self.vertices):
            for j in range(self.vertices):
                if i != j and j not in self.adj_list[i]:
                    return False
        return True
    def list(self):
        return self.adj_list

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
    print(g.list())
    if g.is_complete():
        print("The graph is a complete graph.")
    else:
        print("The graph is not a complete graph.")
