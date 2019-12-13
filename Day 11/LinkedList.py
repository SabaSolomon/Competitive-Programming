class LinkedNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def mergeTwoList(self, l1,l2):
        head = ListNode(0)
        next1 = l1
        next2 = l2 
        if(l1 is None and l2 is None):
            return head.next
        elif(l1 is None): 
            return l2
        elif(l2 is None):
            return l1
        
        if(l1.val > l2.val):
            head.next = next2
            next2 = next2.next
        else:
            head.next = next1
            next1 = next1.next
        currHead = head.next
        while(next1 is not None and next2 is not None):
            if(next1.val>=next2.val):
                currHead.next = next2
                currHead = currHead.next
                next2 = next2.next
            else:
                currHead.next = next1
                currHead = currHead.next
                next1 = next1.next
        if(next1 is not None):
            currHead.next = next1
        elif(next2 is not None):
            currHead.next = next2
        return head.next
    
    def deleteDuplicates(self, head):
        prev = head
        currHead = None
        newPrev = prev
        if(head is None or head.next is None):
            return prev
        currHead = head.next
        while(currHead is not None):
            
            if(newPrev.val == currHead.val):
                newPrev.next = currHead.next
            else:
                newPrev = newPrev.next
            currHead = currHead.next
        return prev
        
class LinkedList:
    def __init__(self):
        self.head = None
    def addNode(self, node):
        if(self.head is None):
            self.head = node
        else:
            check = self.head
            while(check != None):
                if(check.next == None):
                    check.next = node
                    break;
                check = check.next
                
    def removeNode(self, node):
        check = self.head
        prev = None
        while(check is not None):
            if(check.data == node.data and prev is not None):
                prev.next = check.next
                break
            elif(check.data == node.data and prev is None):
                if(check.next is not None):
                    self.head = check.next

            prev = check
            check = check.next
           
            
    def reverse(self):
        prev = None
        curr = self.head
        next = None
        
        
        if(curr is None):
            return check
        while(curr is not None):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            
        self.head = prev
            
       
        
     
            
    def printList(self):
        check = self.head
        while(check is not None):
            print(check.data,"->",end=" ")
            check = check.next
        print(check)
            
linklist = LinkedList()

newNode = LinkedNode(4)
linklist.addNode(newNode)

newNode1 = LinkedNode(5)
linklist.addNode(newNode1)

newNode2 = LinkedNode(6)
linklist.addNode(newNode2)

linklist.printList()
print("\nRemove\n")

linklist.removeNode(newNode1)

print("\nReverse\n")

linklist.printList()

linklist.reverse()
linklist.printList()
link2 = LinkedList()

newNode3 = LinkedNode(1)
link2.addNode(newNode3)


link2.addNode(newNode3)
link2.addNode(newNode3)


