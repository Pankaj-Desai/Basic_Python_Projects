class File:
    def __init__ (self):
        self.content=None 
    
    def Search_Bolck(self, key):
        fi=open("indexfile.txt","r")
        for i in fi:
            temp=i.split(" ")
            if int(temp[0])>=int(key):
                fi.close()
                return[1]
    
    def write_file(self):
        self.content=input("Enter the employee number, name, designation and salary (Ex: 100 ABC Pragrammer 90000): ").split()
        block=self.Search_Bolck(self.content[0])
        f=open(block.rstrip(), "a")
        f.write(self.content[0]+" "+self.content[1]+" "+self.content[2]+" "+self.content[3]+"\n")
        f.close()
  
    def read_file(self):
        f=open("file1.txt", "r")
        print(f.readlines())
        f.close
        f=open("file2.txt", "r")
        print(f.readlines())
        f.close
        f=open("file3.txt", "r")
        print(f.readlines())
        f.close
        f=open("file4.txt", "r")
        print(f.readlines())
        f.close
    
    def search_file(self):
        found=0
        data=input("Enter the enployee number to search his record\n")
        block=self.Search_Bolck(data)
        f=open(block.rstrip(), "r")
        for i in f :
            temp=i.split(" ")
            if temp[0]==data:
                print(temp)
                found=1
                break
        if found==0:
            print("Record does not found!!")
        f.close()
    
    def search_content_file(self,cont,flag):
        l_count=0
        found=0
        temp=cont
        temp1=cont.split()
        block=self.Search_Bolck(temp1[0])
        f=open(block.rstrip(),"r")
        cont=temp
        lines=f.readlines()
        for i in lines:
            l_count+=1
            temp=i.split(" ")
            if temp1[0]==temp[0]:
                if flag==1:
                    lines[l_count-1]=cont+"\n"
                    found=1
                    break
                else:
                    lines[l_count-1]=" "
                    found=1
                    break
            if found==0:
                print("Record not found to update/delete")
            f.close()
            return block,lines
    
    def update_file(self):
        cont=input("Enter employee number with all details to update employee record\n")
        block,lines=self.search_content_file(cont,1)
        with open(block.rstrip(), "w") as f:
            f.writelines("%s" % l for l in lines)
    
    def delete(self):
        cont=input("Enter the employee number to delete employee record\n")
        block,lines=self.search_content_file(cont, 0)
        with open(block.rstrip(), "w") as f:
            f.writelines("%s" % l for l in lines)

fp=File()
while True:
    print("============================================")
    print("Enter 1: Create file or write into it.")
    print("Enter 2: Read the full content of all files")
    print("Enter 3: Seacrh any employee record")
    print("Enter 4: Update record")
    print("Enter 5: Delete employee record from file")
    print("Enter 6: Exit")
    print("============================================")
    ans=int(input("Enter your choice: "))
    if ans==1:
        fp.write_file()
    elif ans==2:
        fp.read_file()
    elif ans==3:
        fp.search_file()
    elif ans==4:
        fp.update_file()
    elif ans==5:
        fp.delete()
    else:
        break
