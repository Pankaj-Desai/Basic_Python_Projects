class Node:
    def __init__ (self,data):           
        self.data=data
        self.left=None 
        self.right=None
        
def Insert(node,data):
    if node is None:
        node=Node(data)
        return node
    elif data<node.data:
        node.left=Insert(node.left,data)
    else:
        node.right=Insert(node.right,data)
    return node

def Display(node):
    if node is not None:
        Display(node.left)
        print(node.data)
        Display(node.right)
        
def DisplayLeaf(node):
    if node is not None:
        if node.left == None and node.right == None:
            print(node.data)
        DisplayLeaf(node.left)
        DisplayLeaf(node.right)

def BFS(node):
    queue=[]
    if node is None:
        return
    queue.append(node)
    while queue:
        temp=queue.pop(0)
        print(temp.data+" ")
        if temp.left:
            queue.append(temp.left)
        if temp.right:
            queue.append(temp.right)
    
def height(node):
    if node is None:
        return 0
    else:
        leftht=0
        rightht=0
    if node.left is not None :
        leftht=height(node.left)
    if node.right is not None:
        rightht=height(node.right)
    if leftht>rightht:
        maximum=leftht
    else:
        maximum=rightht
    
    return maximum+1
    
def mirror(node):
    if node is not None:
        Display(node.right)
        print(node.data)
        Display(node.left)
    
root=None
while True:
    print("\nPress 1 to Insert the node")
    print("Press 2 to Display all the inputs")
    print("Press 3 to Display leaf node of the tree")
    print("Press 4 to do Breadth First Search")
    print("Press 5 to find Height of the tree")
    print("Press 6 to find Mirror Image")
    print("Press 7 to Exit the Application")
    a=int(input("Answer : "))
    if a==1:
        data=input("Enter Number :")
        print("Number = "+data+"\n\n")
        root=Insert(root,data)
    elif a==2:
        print("Numbers in tree are :\n")
        Display(root)
    elif a==3:
        print("Numbers at leaf nodes in tree are :\n")
        DisplayLeaf(root)
    elif a==4:
        BFS(root)
    elif a==5:
        ht=height(root)
        print("Height = "+str(ht))
    elif a==6:
        mirror(root)
    else:
        break