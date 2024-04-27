"""8. Write a Program to accept a directed graph G and compute the in-degree and out-degree of each vertex."""
class DirectedGraph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = [[] for _ in range(vertices)]

    def add_edge(self, u, v):
        self.adj_list[u].append(v)

    def compute_degrees(self):
        in_degrees = [0] * self.vertices
        out_degrees = [0] * self.vertices

        for u in range(self.vertices):
            for v in self.adj_list[u]:
                out_degrees[u] += 1
                in_degrees[v] += 1

        return in_degrees, out_degrees

# Example usage
if __name__ == "__main__":
    num_vertices = 6
    g = DirectedGraph(num_vertices)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 3)
    g.add_edge(3, 4)
    g.add_edge(4, 5)

    print("Vertex\tIn-Degree\tOut-Degree")
    in_degrees,out_degrees=g.compute_degrees()
    for v in range(num_vertices):
        print(f"{v}\t{in_degrees[v]}\t\t{out_degrees[v]}")