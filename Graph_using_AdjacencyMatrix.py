from collections import defaultdict
from pylint import graph

class Dictionary:
    def __init__(self):
        self.graph=defaultdict(list)
    def add(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    def DFS(self):
        visited={}
        stack=[]
        n=input("Enter the start point: ")
        stack.append(n)
        for i in self.graph:
            visited[i]=0
        print("DFS is: ")
        while(stack):
            v=stack.pop()
            if visited[v]==0:
                print(v, end=' ')
                visited[v]=1
                for k in self.graph[v]:
                    if (visited[k]==0):
                        stack.append(k)
        print("\n")
    def BFS(self):
        visited={}
        queue=[]
        for i in self.graph:
            visited[i]=0
        n=input("Enter the start point: ")
        queue.append(n)
        visited[n]=1
        print("BFS is: ")
        while(queue):
            v=queue.pop(0)
            print(v, end=' ')
            for k in self.graph[v]:
                if (visited[k]==0):
                    queue.append(k)
                    visited[k]=1
        print("\n")
    
g=Dictionary()
visited={}
while True:
    print("Press 1 to creat the dictionary")
    print("Press 2 for DFS")
    print("Press 3 for BFS")
    print("Press 4 to exit")
    a=input("Answer: ")
    if a=='1':
        u=input("Enter the start vertex: ")
        v=input("Enter the end vertex: ")
        g.add(u,v)
    elif a=='2':
        g.DFS()
    elif a=='3':
        g.BFS()
    else:
        break
