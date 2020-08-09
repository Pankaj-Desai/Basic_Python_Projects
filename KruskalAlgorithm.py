parent={}
class Graph:
    def __init__(self,vertex):
        self.MAX = vertex
        self.graph = []
    
    def accept_graph(self, u, v ,wt):
        self.graph.append([u, v, wt])
        print("Adjcentcy list:\n" + str(self.graph))
        if u not in parent:
            parent[u] = 0
        if v not in parent:
            parent[v] = 0
    def find(self, i):
        while(parent[i]):
            i = parent[i]
        return i
    def uni (self, u, v):
        if u!=v:
            parent[v] = u
            return 1
        else:
            return 0

    def kruskal(self):
        self.graph = sorted(self.graph, key=lambda item: item[2])
        print(self.graph)
        cost=0
        for edge in self.graph:
            v1=edge[0]
            v2=edge[1]
            u=self.find(v1)
            v=self.find(v2)
            if self.uni(u,v):
                cost=cost+edge[2]
                print(v1, "-->", v2, "=", str(edge[2]))
        print("MST cost is: "+str(cost))

n=int(input("Enter the number of the vertex: "))
g=Graph(n)
while True:
    print("========================================")
    print("MST using kruskal algorith")
    print("1) Accept the graph\n2)Mininum Spaning Tree\n3)Exit")
    ans = int(input("Answer: "))
    if ans==1:
        edge = input("Enter the edge and weight(a-b-weight)")
        inp = edge.split("-")
        g.accept_graph(inp[0],inp[1], int(inp[2]))
        print(parent)
    elif ans==2:
        g.kruskal()
    else:
        break
