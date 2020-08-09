def heapSort(arr): 
    n = len(arr) 
  
    # Build a maxheap. 
    for i in range(n, -1, -1): 
        heapify(arr, n, i) 
  
    # One by one extract elements 
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i]   # swap 
        heapify(arr, i, 0) 
def heapify(arr, n, i): 
    largest = i  # Initialize largest as root 
    l = 2 * i + 1     # left Child= 2*i + 1 
    r = 2 * i + 2     # right Child= 2*i + 2 
  
    # if left child of root exists and is greater than root 
    if l < n and arr[i] < arr[l]: 
        largest = l 
  
    # if right child of root exists and is greater than root 
    if r < n and arr[largest] < arr[r]: 
        largest = r 
# make largest element as root 
    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i]  # swap 
  
        # Heapify the root. 
        heapify(arr, n, largest) 
arr = [] 
print("Program for Heap Sort")
while 1:
    ch=int(input("  1.Accpet \n 2.Heapsort \n 3.exit \n Enter Choice \n"))
    if(ch==1):
        n = int(input("Enter number of elements : ")) 
        for i in range(0, n): 
            ele = int(input()) 
            arr.append(ele)
        print(arr) 
    elif(ch==2):
        heapSort(arr) 
        n = len(arr) 
        print ("Sorted array is") 
        for i in range(n): 
            print ("%d" %arr[i]), 
    else:
        print("Exit")
        break