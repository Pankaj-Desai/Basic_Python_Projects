class Node:
    def __init__ (self,data):           
        self.data=data
        self.left=None 
        self.right=None
        self.lth=1
        self.rth=1
        
def insert(lroot,temp):
    if temp.data<lroot.data:
        if lroot.lth==1:
            temp.left=lroot.left
            temp.right=lroot
            lroot.left=temp
            lroot.lth=0
        else:
            insert(lroot.left,temp)
    elif temp.data>lroot.data:
        if lroot.rth==1:
            temp.right=lroot.right
            temp.left=lroot
            lroot.right=temp
            lroot.rth=0
        else:
            insert(lroot.right,temp)

def inorder(temp,headernode):
    while(temp != headernode):
        while(temp.lth == 0):
            temp=temp.left
        print(temp.data, end=' ')
        while(temp.rth == 1):
            temp=temp.right
            if temp == headernode:
                break
            print(temp.data, end=' ')
        temp=temp.right

def preorder(temp,headernode):
    while(temp != headernode):
        print(temp.data, end=' ')
        while(temp.lth == 0):
            temp=temp.left
            print(temp.data, end=' ')
        while(temp.rth == 1):
            temp=temp.right
            if temp == headernode:
                break
        temp=temp.right

root=hNode=None
hNode=Node("999")


print("Threaded Binary Search Tree")
while True:
    print("1 to Insert")
    print("2 for Inorder Traversal")
    print("3 for Preorder Traversal")
    print("4 for Postorder Traversal")
    n=int(input("Answer : "))
    if n==1:
        key=input("Enter Node Value : ")
        temp=Node(int(key))
        if root is None:
            root=temp
            hNode.left=root
            hNode.right=hNode
            root.left=hNode
            root.right=hNode
        else:
            insert(root,temp)
    elif n==2:
        print("Inorder Traversal : ")
        inorder(root,hNode)
        print()
    elif n==3:
        print("Preorder Traversal : ")
        preorder(root,hNode)
        print()
    elif n==4:
        print("Postorder Traversal : ")
        postorder(root,hNode)
        print()
    else:
        print("Wromg Input!!!!")
