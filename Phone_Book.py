                                                                    #Phonebook using Hash Table#



#"defaultdict" is first imported from the collections
from collections import defaultdict
count=0                                #for checking table size
class HashTable:
    def __init__ (self, size):
        self.HashTab=defaultdict(list)
        for i in range (size):
            self.HashTab[i]=[]
        self.display()

    def hashing(self,name):                             #Hash function 
        sum=0
        l=len(name)
        for i in range (0,l):
            sum=sum+ord(name[i])
        return(sum%size)

    def insert_record(self,pos,nm,ph):                      #direct insertion without replacement
        global count
        if len(self.HashTab[pos])==0:
            self.HashTab[pos].append(nm)
            self.HashTab[pos].append(ph)
            count=count+1
        elif self.HashTab[pos][0]==nm:
            self.HashTab[pos].append(ph)
        else:
            self.find_next_vacant_pos(pos, nm, ph)
    
    def find_next_vacant_pos(self,pos,nm,ph):                   #Finds next vacant position in the table 
        global count
        for i in range (1,size):
            z=(pos+i)%size
            if len(self.HashTab[z])==0:
                self.HashTab[z].append(nm)
                self.HashTab[z].append(ph)
                count=count+1
                break
    
    def wreplace(self,pos,nm,ph):                           #Insertion with replacement 
        global count
        if len(self.HashTab[pos])==0:
            self.HashTab[pos].append(nm)
            self.HashTab[pos].append(ph)
            count=count+1
        elif self.HashTab[pos][0]==nm:
            self.HashTab[pos].append(ph)
        elif pos==self.hashing(self.HashTab[pos][0]):
            self.find_next_vacant_pos(pos,nm,ph)
        else:
            temp=self.HashTab[pos]
            self.HashTab[pos]=[]
            self.HashTab[pos].append(nm)
            self.HashTab[pos].append(ph)
            self.find_next_pos(pos,temp)
    
    def find_next_pos(self,pos,temp):                                       #Find next position in the table 
        global count
        for i in range (1,size):
            z=(pos+i)%size
            if len(self.HashTab[z])==0:
                self.HashTab[z]=temp
                count=count+1
                break
    
    def display(self):                                              #Displays full hash table
        print("******Hash Table******")
        for i in sorted (self.HashTab.items()):
            print(i)
    
    def search(self,nm):                                    #Search perticular name in the table
        flag=0
        pos=h.hashing(nm)
        if len(self.HashTab[pos])!=0 and self.HashTab[pos][0]==nm:
            print("\nRecord for "+ nm +" found !!")
            print(self.HashTab[pos])
        else:
            for i in range (1,size):
                z=(pos+i)%size
                if len(self.HashTab[z])!=0 and self.HashTab[z][0]==nm:
                    print("\nRecord for "+ nm +" found at "+ str(z))
                    print(self.HashTab[z])
                    flag=1
                    break
            if flag==0:
                print("\nRecord for "+ nm +" not found")

#MANI CODING
size=int(input("Enter the Telephone book size: "))
while True:
    print("\n\n***Telephone Dictionary***")
    print("1)Add new record without replacement")
    print("2)Add new record with replacement\n3)display all records\n4)Search any record\n5)Exit phonebook")
    a=int(input("Answer: "))
    if a==1:                                #Without relacement
        h=HashTable(size)
        count=0
        while True:
            name=str.strip(input("Enter the name: "))
            name=name.upper()
            phnumber=int(input("Enter the phonenumber: "))
            pos=h.hashing(name)
            h.insert_record(pos,name,phnumber)
            h.display()
            opt=int(input("Do you want to add more elements(1-YES/0-NO): "))
            if opt==1:
                if (count==size):
                    print("Phonebook is full !! can not add more elements")
                    break
            else:
                break
    elif a==2:                      #with replacement
        h=HashTable(size)
        count=0
        while True:
            name=str.strip(input("Enter the name: "))
            name=name.upper()
            phnumber=int(input("Enter the phone number: "))
            pos=h.hashing(name)
            h.wreplace(pos,name,phnumber)
            h.display()
            opt=int(input("Do you want to add more elements(1-YES/0-NO): "))
            if opt==1:
                if (count==size):
                    print("Phonebook is full !! can not add more elements")
                    break
            else: 
                break
    elif a==3:                       #display hash table 
        h.display()
    elif a==4:                              #search perticular name 
        name=str.strip(input("Enter the name: "))
        h.search(name.upper())
    else:                               #exit phonebook
        break