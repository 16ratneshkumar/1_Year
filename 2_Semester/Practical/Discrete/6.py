"""6. Write a Program to check if a given graph is a complete graph. Represent the 
graph using the Adjacency Matrix representation."""
class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_matrix = [[0] * vertices for _ in range(vertices)]

    def add_edge(self, u, v):
        if graph_type== 1:
            self.adj_matrix[u][v] = 1
            self.adj_matrix[v][u] = 1
        else:
            self.adj_matrix[u][v] = 1

    def is_complete(self):
        for i in range(self.vertices):
            for j in range(self.vertices):
                if i != j and self.adj_matrix[i][j] == 0:
                    return False
        return True
    def get_matrix(self):
        return self.adj_matrix

if __name__ == "__main__":
    graph_type =int(input("Enter Your Graph Type(1.Undirected 2.Directed)::"))
    num_vertices = int(input("Enter number of vertices::"))
    g = Graph(num_vertices)
    num=int(input("Enter number of edges::"))
    for i in range(num):
        a=int(input(f"Enter first vertice of {i+1} edge:: "))- 1
        b=int(input(f"Enter second vertice of same edge:: "))- 1
        g.add_edge(a,b)
    print("Your Adjacency Matrix is::\n",g.get_matrix())
    if g.is_complete():
        print("The graph is a complete graph.")
    else:
        print("The graph is not a complete graph.")
