import math
from random import randrange

def insertionSort(list):
    for i in range(0, len(list)):
        if(i < len(list)-1):
            for j in range(i+1, len(list)):
                if(list[i] >list[j]):
                    list[i], list[j] = list[j],list[i]
    return list
                   
#print(insertionSort([1, 3, 9, 3, 4]))

def selectionSort(list):
    for i in range(0, len(list)):
        min = list[i];
        for j in range(i, len(list) - 1):
            if(list[j] < list[j - 1]):
                min = list[j]
        list[i] = min
    return list

#print(selectionSort([1, 3, 9, 3, 5, 8]))


def mergeSort(arr): 
    if len(arr) > 1: # base case
        mid = len(arr)//2 
        L = arr[:mid] 
        R = arr[mid:] 
  
        mergeSort(L) 
        mergeSort(R)
  
        i = j = k = 0
        
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+=1
            else: 
                arr[k] = R[j] 
                j+=1
            k+=1
            print(arr)
          
       
        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1
    return arr
    
            
#arr = [3,4,5,8,6,1]          
#print(mergeSort(arr))

def countingSort(list):
    count = 0
    max = list[0]
    for i in list:
        if(i > max):
            max = i
    counter = []
    order = []
       
    for i in range(0, max+1):
        counter.insert(i, 0)
    for j in range(0, len(list)):
        counter[list[j]] += 1
    for k in range(0, max+1):
        if(counter[k] != 0):
            for l in range(0, counter[k]):
                order.insert(count, k)
                count+=1
    return order
            
#print(countingSort([2,5,9,9,3,4]))

def randomizeList(num):
    list = []
    for i in range(0, num+1):
        list.insert(i, i)
    for j in range(0, num+1):
        n = num+1
        rand_index = randrange(n)
        list[j], list[rand_index] = list[rand_index], list[j]
    return list
        
#print(randomizeList(10))  
        
 

# Using a median of three
def quickSort(list):
    quickSortList(list, 0, len(list)-1)
    return list
    
def quickSortList(list, begin, end):
    if(begin < end):
        p = partition(list, begin, end)  # returns the pivot
        quickSortList(list, begin, p-1)
        quickSortList(list, p+1, end)
        
def getPivot(list, begin, end):
    mid = (begin+end)//2
    pivot = end
    
    if(list[begin]<list[mid]):
        if(list[mid]<list[end]):
            pivot = mid
    elif(list[end] > list[begin]):
        pivot = begin
        
    return pivot

def partition(list, begin, end):

    pivot = getPivot(list, begin, end)
    pivotValue = list[pivot]

    list[begin], list[pivot] = list[pivot], list[begin]
    border = begin
   
    for i in range(begin+1, end+1):
        if(list[border] > list[i]):
            border+=1
            list[border], list[i] = list[i], list[border]
            
            
    list[begin], list[border] = list[border], list[begin]  # return pivot to position

    
    return border

print(quickSort([3,9,5,8,6,7,4,3]))      
    

