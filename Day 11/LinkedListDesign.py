class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None
class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        count = 0
        temp = self.head
        while(temp is not None):
            if(count == index):
                return temp.val
            temp = temp.next
            
            count+=1
        return -1

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        temp = self.head
        node = Node(val)
        node.next = temp
        self.head = node
        

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        print("\n------tail------")
        temp = self.head
        while(temp is not None):
            if(temp.next is None):
                temp.next = Node(val)
                break
            temp = temp.next
        t=self.head
        while(t is not None):
            print(t.val,end="->")
            t=t.next
            
        
        

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        count = 0
        temp = self.head
        print("\n----------before add-----------")
        t=self.head
        while(t is not None):
            print(t.val,end="->")
            t=t.next
        if(index == 0 and temp is None):
                self.addAtHead(val)
                return
        while(temp is not None):
            if(index == 0):
                self.addAtHead(val)
                break
            if(count + 1 == index and temp.next is not None):
                next = temp.next
                node = Node(val)
                temp.next = node
                node.next = next
                break
            
            count+=1
            if(count == index and temp.next is None):
                self.addAtTail(val)
                break
            temp = temp.next
        
        
        print("\n----------add-----------")
        t=self.head
        while(t is not None):
            print(t.val,end="->")
            t=t.next
        
        

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        count = 0
        temp = self.head
        while(temp is not None):
            if(index == 0):
                self.head = temp.next
                break
            if(count+1 == index and temp.next is not None):
                next = temp.next.next
                temp.next = next
                break
             
            temp = temp.next
            count+=1
        t=self.head
        print("\n------delete----")
        while(t is not None):
            print(t.val,end="->")
            t=t.next
        
        
        


# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
# param_1 = obj.get(index)
#obj.addAtHead(7)
#obj.addAtHead(2)
#obj.addAtHead(1)
obj.addAtIndex(0, 10)
obj.addAtIndex(0, 20)
obj.addAtIndex(0, 30)
print("\n",obj.get(0), end="\n")

#obj.addAtIndex(4, 8)
#obj.deleteAtIndex(4)
#obj.addAtIndex(5, 7)
#obj.addAtIndex(4,8)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
