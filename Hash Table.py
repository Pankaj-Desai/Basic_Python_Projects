'''This is the small sample of how to creat our 
own Hash Table using python and Thanks for selecting my code'''


#'defaultdict' is imported form the dictionary
from collections import defaultdict         
count=0             #For checking table is fulled 75% or not
class HashTable:
    def __init__(self, size):
        self.hashTab=defaultdict().fromkeys(range(size), -1)
    def hashing(self, key):             #Hash function is created for hashing purpose 
        return(key % size)
    def woreplace(self, key, pos):                 #Function defined for "Without Replacement Hashing"
        global count
        if self.hashTab[pos]== -1:
            self.hashTab[pos]= key
            count=count+1
        else:
            self.find_next_vacant_pos(key,pos)
    def find_next_vacant_pos(self,key,pos):         #For finding next vacant positon in the hash table
        global count
        for i in range (1, size):
            z=(key+i)%size
            if self.hashTab[z]== -1:
                self.hashTab[z] =key
                count=count+1
                break
    def wreplace(self,key,pos):                 #Function defined for "With Replacement Hashing"
        global count
        if self.hashTab[pos]== -1:
            self.hashTab[pos] =key
            count=count+1
        elif pos==self.hashing(self.hashTab[pos]):
            self.find_next_vacant_pos(key,pos)
        else:
            temp=self.hashTab[pos]
            self.hashTab[pos]=key
            self.find_next_vacant_pos(temp,pos)
    def display(self):                              #For displaying whole hash table 
        print("\n**********Hash Table**********")
        for i in self.hashTab.items():
            print(i)
        print("******************************\n\n")
    def search(self,key):                           #for searching any perticular key form the hash table
        flag=0
        pos=self.hashing(key)
        if self.hashTab[pos]==key:
            print(str(key)+" found at its home address ! !\n")
        else:
            for i in range(size):
                z=(key+i)%size
                if self.hashTab[z]==key:
                    print(str(key)+" found at address "+str(z)+"\n")
                    flag=1
                    break
            if flag==0:
                print(str(key)+" is not present in the Hash Table\n")
#Main Coding
print("Collision Handling")
size=int(input("Enter the Table size: "))
while 1:
    print("1)Without Replacement\n2)With Replacement\n3)Display\n4)Search\n5)Exit")
    a=int(input("Answer= "))
    if a==1:
        h=HashTable(size)
        count=0
        while True:
            key=int(input("Enter the Key: "))
            pos=h.hashing(key)
            h.woreplace(key,pos)
            h.display()
            opt=int(input("Do you want to add more element (1 for Yes / 0 for No): "))
            if opt==1:
                if (count*100 / size) >= 80:
                    print("Hash Table is nearly full !! cannot add more elements")
                    break
            else:
                break
    elif a==2:
        h=HashTable(size)
        count=0
        while True:
            key=int(input("Enter the Key: "))
            pos=h.hashing(key)
            h.wreplace(key,pos)
            h.display()
            opt=int(input("Do you want to add more element (1 for Yes / 0 for No): "))
            if opt==1:
                if (count*100 / size) >= 80:
                    print("Hash Table is nearly full !! cannot add more elements")
                    break
            else:
                break
    elif a==3:
        print("\n")
        h.display()
    elif a==4:
        id=int(input("\nEnter the value to search: "))
        h.search(id)
    else:
        break
