class Node:                                     #Class is created for making Tree
    def __init__ (self,word,meaning):           
        self.word=word
        self.meaning=meaning
        self.left=None 
        self.right=None 

def Insert(node,word,meaning):                  #Function is created for the insertion of word in the Dictionary
    if node is None:
        node=Node(word,meaning)
        return node
    elif word<node.word:
        node.left=Insert(node.left,word,meaning)
    else:
        node.right=Insert(node.right,word,meaning)   
    return node

def Display(node):                     #Function is created for the displaying all the words and its meaning from Dictionary
    if node is not None:                           
        Display(node.left)
        print(node.word+" : "+node.meaning)
        Display(node.right)

def Search(node,word,count):                #Function is created to search a perticular word in the Dictionary
    if node is None:
        return None
    elif word==node.word :
        count=count+1
        print("Number of iterations will be: "+str(count))
        return node
    elif word<node.word :
        count=count+1
        return Search(node.left,word,count)
    else:
        count=count+1 
        return Search(node.right,word,count)

def Update(node,word,meaning):                 #Function is created to update a particular word in the Dictionary
    if node is None:
        return None
    elif word==node.word :
        node.meaning=meaning
        print("\nMeaning is updated")
        return node
    elif word<node.word :
        return Update(node.left,word,meaning)
    else:
        return Update(node.right,word,meaning)

def FindMin(node):                          #To find Maximum value in that perticular tree
    while node.right:
        node=node.right
    return node

def deletenode(node,word):                  #Function is created to delete a particular word for the Dictionary
    if (node is None):
        return None
    elif (word<node.word):  
        node.left=deletenode(node.left,word)
    elif (word>node.word):
        node.right=deletenode(node.right,word)
    else:                           
        if node.left is None:                   #If node is "Leaf Node" or have only one child
            temp=node.right
            node=None
            print("\nWord is deleted..!")
            return temp
        elif node.right is None:                 #If node is "Leaf Node" or have only one child
            temp=node.left
            node=None
            print("\nNode is deleted..!")
            return temp
        else:                                   #If that node have two children
            temp=FindMin(node.right)
            print(temp.word)
            node.word=temp.word
            node.meaning=temp.meaning
            node.right=deletenode(node.right,temp.word)
    return node
  
root=None                                    #Value of "root" is asigned an zero OR none
while True:                                 #While loop is used as switch case here 
    print("\n\nPress 1 to Insert the word and its meaning in the Dictionary")
    print("Press 2 to Display the words and its meanings in the Dictionary")
    print("Press 3 to Search the meaning of any word in the Dictionary")
    print("Press 4 to Update the data in the Dictionary")
    print("Press 5 to Delete any word in the Dictionary")
    print("Press 6 to Exit the Dictionary\n")
    a=int(input("\nAnswer= "))
    if a==1:                            #For insertion of the word
        string=input("\nEnter the word and its meaning: ").split()
        word=string[0]
        meaning=string[1]
        print("\nWord is: "+word+" and its meaning is: "+meaning+"\n")
        root=Insert(root,word,meaning)              #Function is called
    elif a==2:                          #For Displaying all the words from the Dictionary
        Display(root)
    elif a==3:                          #For Searching a word
        count=0                         #"Count" is used to count the iterations used to search that particular word
        word=input("\nWhich word you want to search: ")
        found=Search(root,word,count)   #Function is called
        if found is None:
            print("\nSORRY,their is no such Word")
        else:
            print(found.word+" : "+found.meaning)
    elif a==4:                           #For Updating the meaning of a word
        UpWord=input("\nWhose meaning do you want to update: ")
        UpMeaning=input("\nWhat is the updated meaning: ")
        update=Update(root,UpWord,UpMeaning)                #Function is called    
    elif a==5:
        delete=input("Enter the word you want to delete: ")
        deleted=deletenode(root,delete)
    else:                                           #Takes exit from the application 
        break
