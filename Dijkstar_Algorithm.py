vertices=[]
parent={}
visited={}
dist={}
class Graph:
    def __init__(self, n):
        self.MAX=n
        self.graph=[]
    
    def creat_graph(self, u, v, wt):
        self.graph.append([u,v,wt])
        print("Adjacency MAtrix:\n"+str(self.graph))
        if u not in vertices:
            vertices.append(u)
        if v not in vertices:
            vertices.append(v)

    def initialize(self):
        for v in vertices:
            parent[v]=visited[v]=0
            dist[v]=999
        
    def find_weight(self, curr, v):
        flag=0
        for edge in self.graph:
            if edge[0]==curr and edge [1]==v:
                flag=1
                break
        if flag:
            return edge[2]
        else:
            return 999
    def Shortest_path(self, s, t):
        self.initialize()
        visited[s]=1
        dist[s]=0
        curr=s
        while curr!=t:
            smalldist=999
            dc=dist[curr]
            for v in vertices:
                if visited[v]==0:
                    wt=self.find_weight(curr,v)
                    newDist=dc+wt
                    if newDist<dist[v]:
                        dist[v]=newDist
                        parent[v]=curr
                    if dist[v]<smalldist:
                        smalldist=dist[v]
                        k=v
            curr=k
            visited[curr]=1
        self.displayPath(s, t)
    
    def displayPath(self,s,t):
        path=[]
        print("Shortest distance: "+str(dist[t]))
        path.append(t)
        while(t!=s):
            t=parent[t]
            path.append(t)
        print("Shortest path is: ")
        shortestPath=path[::-1]
        for ele in shortestPath:
            print(ele,"-->",end="")

n=int(input("Enter the number of the vertices: "))
g=Graph(n)
while True:
    print("======================================")
    print("Shortest path using Dijkstar Algorithm")
    print("1) Accept the graph\n2) Shortest Path\n3) Exit")
    print("======================================")
    ans=int(input("Answer: "))
    if ans==1:
        edge=input("Enter the edge and the weight(a-b-weigth)")
        inp=edge.split("-")
        g.creat_graph(inp[0],inp[1],int(inp[2]))
    elif ans==2:
        vertices.sort()
        print(vertices)
        while 1:
            s=input("Enter the source vertex: ")
            t=input("Enter the  target vertex: ")
            g.Shortest_path(s,t)
            ch=input("\nWant to check another path (y/n)")
            if ch=='n':
                break
    else:
        break