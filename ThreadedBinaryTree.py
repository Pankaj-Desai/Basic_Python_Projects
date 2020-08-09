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

def Inorder(temp,headernode):
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

def Preorder(temp,headernode):
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
hNode.right=hNode

while True:
    print("\nWhat do you want to do ?")
    print("1) Insert the elements in the TBT")
    print("2) Display the elements form TBT")
    print("3) Exit the application")
    a=input("Answer: ")
    if a=="1":
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
    elif a=="2":
        while True:
            print("\nHow do you want to print the tree ?")
            print("1) Inorder")
            print("2) Preorder")
            b=input("Answer: ")
            if b=="1":
                Inorder(root,hNode)
                break
            elif b=="2":
                Preorder(root,hNode)
                break
            else:
                break
    else:
        break    
