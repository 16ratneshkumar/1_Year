"""7. Write a Program to check if a given graph is a complete graph. Represent the 
graph using the Adjacency List representation."""
class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = [[] for _ in range(vertices)]

    def add_edge(self, u, v):
        if graph_type== 1:
            self.adj_list[u].append(v)
            self.adj_list[v].append(u)
        else:
            self.adj_list[v].append(u)

    def is_complete(self):
        for i in range(self.vertices):
            for j in range(self.vertices):
                if i != j and j not in self.adj_list[i]:
                    return False
        return True
    def get_list(self):
        return self.adj_list

if __name__ == "__main__":
    graph_type =int(input("Enter Your Graph Type(1.Undirected 2.Directed)::"))
    num_vertices = int(input("Enter number of vertices::"))
    g = Graph(num_vertices)
    num=int(input("Enter number of edges::"))
    for i in range(num):
        a=int(input(f"Enter first vertice of {i+1} edge:: "))
        b=int(input(f"Enter second vertice of same edge:: "))
        g.add_edge(a,b)
    print("Your Adjacency Matrix is::\n",g.get_list())
    if g.is_complete():
        print("The graph is a complete graph.")
    else:
        print("The graph is not a complete graph.")
