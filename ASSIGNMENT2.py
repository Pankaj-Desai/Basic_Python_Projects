class TreeNode:
    def __init__(self,value):
        self.value=value
        self.right=None
        self.left=None
        
def isOperator(c):
    if (c == '+' or c == '-' or c == '*' or c == '/' or c == '^'): 
        return True
    else: 
        return False
    
def peek(stack): 
    if len(stack) > 0: 
        return stack[-1] 
    return None
    
def buildTree(prefix):
    prefix=prefix[::-1]
    stack=[]
    for char in prefix:
        if not isOperator(char):
            t=TreeNode(char)
            stack.append(t)
        else:
            t=TreeNode(char)
            t.left=stack.pop()
            t.right=stack.pop()
            stack.append(t)
    return stack.pop()

def inorderRec(node):
    if node is not None:
        inorderRec(node.left)
        print(node.value, end=' ')
        inorderRec(node.right)
        
def inorder(node):
    current=node
    nodeStack=[]
    while True:
        if current is not None:
            nodeStack.append(current)
            current=current.left
        elif(nodeStack):
            current=nodeStack.pop()
            print(current.value, end=' ')
            current=current.right
        else:
            break
        
def postorderRec(node):
    if node is not None:
        postorderRec(node.left)
        postorderRec(node.right)
        print(node.value, end=' ')

def postorder(node):
    if node is None: 
        return
    stack = [] 
    while(True):
        while (node):
            if node.right is not None: 
                stack.append(node.right) 
            stack.append(node) 
            node = node.left 
        node = stack.pop() 
        if (node.right is not None and peek(stack) == node.right): 
            stack.pop() 
            stack.append(node) 
            node = node.right   
        else: 
            print(node.value, end=' ')  
            node = None
        if (len(stack) <= 0): 
                break

def preorderRec(node):
    if node is not None:
        print(node.value, end=' ')
        preorderRec(node.left)
        preorderRec(node.right)

def preorder(root):
    if root is None:
        return
    nodeStack=[]
    nodeStack.append(root)
    while(len(nodeStack)>0):
        node=nodeStack.pop()
        print(node.value, end=' ')
        if node.right is not None:
            nodeStack.append(node.right)
        if node.left is not None:
            nodeStack.append(node.left)

prefix=input("Enter the Prefix Expression : ")
root =buildTree(prefix)
while True:
    print("\n\nEnter 1 to print infix expression(Recursive)")
    print("Enter 2 to print infix expression(Non-Recursive)")
    print("Enter 3 to print postfix expression(Recursive)")
    print("Enter 4 to print postfix expression(Non-Recursive)")
    print("Enter 5 to print prefix expression(Recursive)")
    print("Enter 6 to print prefix expression(Non-Recursive)")
    print("Enter 7 to Exit the Application")
    num=int(input("Answer : "))
    if num == 1:
        inorderRec(root)
    elif num ==2:
        inorder(root)
    elif num == 3:
        postorderRec(root)
    elif num == 4:
        postorder(root)
    elif num == 5:
        preorderRec(root)
    elif num == 6:
        preorder(root)
    else:
        break
